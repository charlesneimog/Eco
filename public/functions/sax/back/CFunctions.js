var yinModule = typeof yinModule != "undefined" ? yinModule : {};
var moduleOverrides = Object.assign({}, yinModule);
var arguments_ = [];
var thisProgram = "./this.program";
var quit_ = (status, toThrow) => {
    throw toThrow
};
var ENVIRONMENT_IS_WEB = typeof window == "object";
var ENVIRONMENT_IS_WORKER = typeof importScripts == "function";
var ENVIRONMENT_IS_NODE = typeof process == "object" && typeof process.versions == "object" && typeof process
    .versions.node == "string";
var scriptDirectory = "";

function locateFile(path) {
    if (yinModule["locateFile"]) {
        return yinModule["locateFile"](path, scriptDirectory)
    }
    return scriptDirectory + path
}
var read_, readAsync, readBinary, setWindowTitle;

function logExceptionOnExit(e) {
    if (e instanceof ExitStatus) return;
    let toLog = e;
    err("exiting due to exception: " + toLog)
}
if (ENVIRONMENT_IS_NODE) {
    var fs = require("fs");
    var nodePath = require("path");
    if (ENVIRONMENT_IS_WORKER) {
        scriptDirectory = nodePath.dirname(scriptDirectory) + "/"
    } else {
        scriptDirectory = __dirname + "/"
    }
    read_ = (filename, binary) => {
        filename = isFileURI(filename) ? new URL(filename) : nodePath.normalize(filename);
        return fs.readFileSync(filename, binary ? undefined : "utf8")
    };
    readBinary = filename => {
        var ret = read_(filename, true);
        if (!ret.buffer) {
            ret = new Uint8Array(ret)
        }
        return ret
    };
    readAsync = (filename, onload, onerror) => {
        filename = isFileURI(filename) ? new URL(filename) : nodePath.normalize(filename);
        fs.readFile(filename, function(err, data) {
            if (err) onerror(err);
            else onload(data.buffer)
        })
    };
    if (process["argv"].length > 1) {
        thisProgram = process["argv"][1].replace(/\\/g, "/")
    }
    arguments_ = process["argv"].slice(2);
    if (typeof module != "undefined") {
        module["exports"] = yinModule
    }
    process["on"]("uncaughtException", function(ex) {
        if (!(ex instanceof ExitStatus)) {
            throw ex
        }
    });
    process["on"]("unhandledRejection", function(reason) {
        throw reason
    });
    quit_ = (status, toThrow) => {
        if (keepRuntimeAlive()) {
            process["exitCode"] = status;
            throw toThrow
        }
        logExceptionOnExit(toThrow);
        process["exit"](status)
    };
    yinModule["inspect"] = function() {
        return "[Emscripten Module object]"
    }
} else if (ENVIRONMENT_IS_WEB || ENVIRONMENT_IS_WORKER) {
    if (ENVIRONMENT_IS_WORKER) {
        scriptDirectory = self.location.href
    } else if (typeof document != "undefined" && document.currentScript) {
        scriptDirectory = document.currentScript.src
    }
    if (scriptDirectory.indexOf("blob:") !== 0) {
        scriptDirectory = scriptDirectory.substr(0, scriptDirectory.replace(/[?#].*/, "").lastIndexOf("/") +
            1)
    } else {
        scriptDirectory = ""
    } {
        read_ = url => {
            var xhr = new XMLHttpRequest;
            xhr.open("GET", url, false);
            xhr.send(null);
            return xhr.responseText
        };
        if (ENVIRONMENT_IS_WORKER) {
            readBinary = url => {
                var xhr = new XMLHttpRequest;
                xhr.open("GET", url, false);
                xhr.responseType = "arraybuffer";
                xhr.send(null);
                return new Uint8Array(xhr.response)
            }
        }
        readAsync = (url, onload, onerror) => {
            var xhr = new XMLHttpRequest;
            xhr.open("GET", url, true);
            xhr.responseType = "arraybuffer";
            xhr.onload = () => {
                if (xhr.status == 200 || xhr.status == 0 && xhr.response) {
                    onload(xhr.response);
                    return
                }
                onerror()
            };
            xhr.onerror = onerror;
            xhr.send(null)
        }
    }
    setWindowTitle = title => document.title = title
} else {}
var out = yinModule["print"] || console.log.bind(console);
var err = yinModule["printErr"] || console.warn.bind(console);
Object.assign(yinModule, moduleOverrides);
moduleOverrides = null;
if (yinModule["arguments"]) arguments_ = yinModule["arguments"];
if (yinModule["thisProgram"]) thisProgram = yinModule["thisProgram"];
if (yinModule["quit"]) quit_ = yinModule["quit"];
var wasmBinary;
if (yinModule["wasmBinary"]) wasmBinary = yinModule["wasmBinary"];
var noExitRuntime = yinModule["noExitRuntime"] || true;
if (typeof WebAssembly != "object") {
    abort("no native wasm support detected")
}
var wasmMemory;
var ABORT = false;
var EXITSTATUS;
var UTF8Decoder = typeof TextDecoder != "undefined" ? new TextDecoder("utf8") : undefined;

function UTF8ArrayToString(heapOrArray, idx, maxBytesToRead) {
    var endIdx = idx + maxBytesToRead;
    var endPtr = idx;
    while (heapOrArray[endPtr] && !(endPtr >= endIdx)) ++endPtr;
    if (endPtr - idx > 16 && heapOrArray.buffer && UTF8Decoder) {
        return UTF8Decoder.decode(heapOrArray.subarray(idx, endPtr))
    }
    var str = "";
    while (idx < endPtr) {
        var u0 = heapOrArray[idx++];
        if (!(u0 & 128)) {
            str += String.fromCharCode(u0);
            continue
        }
        var u1 = heapOrArray[idx++] & 63;
        if ((u0 & 224) == 192) {
            str += String.fromCharCode((u0 & 31) << 6 | u1);
            continue
        }
        var u2 = heapOrArray[idx++] & 63;
        if ((u0 & 240) == 224) {
            u0 = (u0 & 15) << 12 | u1 << 6 | u2
        } else {
            u0 = (u0 & 7) << 18 | u1 << 12 | u2 << 6 | heapOrArray[idx++] & 63
        }
        if (u0 < 65536) {
            str += String.fromCharCode(u0)
        } else {
            var ch = u0 - 65536;
            str += String.fromCharCode(55296 | ch >> 10, 56320 | ch & 1023)
        }
    }
    return str
}

function UTF8ToString(ptr, maxBytesToRead) {
    return ptr ? UTF8ArrayToString(HEAPU8, ptr, maxBytesToRead) : ""
}

function stringToUTF8Array(str, heap, outIdx, maxBytesToWrite) {
    if (!(maxBytesToWrite > 0)) return 0;
    var startIdx = outIdx;
    var endIdx = outIdx + maxBytesToWrite - 1;
    for (var i = 0; i < str.length; ++i) {
        var u = str.charCodeAt(i);
        if (u >= 55296 && u <= 57343) {
            var u1 = str.charCodeAt(++i);
            u = 65536 + ((u & 1023) << 10) | u1 & 1023
        }
        if (u <= 127) {
            if (outIdx >= endIdx) break;
            heap[outIdx++] = u
        } else if (u <= 2047) {
            if (outIdx + 1 >= endIdx) break;
            heap[outIdx++] = 192 | u >> 6;
            heap[outIdx++] = 128 | u & 63
        } else if (u <= 65535) {
            if (outIdx + 2 >= endIdx) break;
            heap[outIdx++] = 224 | u >> 12;
            heap[outIdx++] = 128 | u >> 6 & 63;
            heap[outIdx++] = 128 | u & 63
        } else {
            if (outIdx + 3 >= endIdx) break;
            heap[outIdx++] = 240 | u >> 18;
            heap[outIdx++] = 128 | u >> 12 & 63;
            heap[outIdx++] = 128 | u >> 6 & 63;
            heap[outIdx++] = 128 | u & 63
        }
    }
    heap[outIdx] = 0;
    return outIdx - startIdx
}

function stringToUTF8(str, outPtr, maxBytesToWrite) {
    return stringToUTF8Array(str, HEAPU8, outPtr, maxBytesToWrite)
}
var buffer, HEAP8, HEAPU8, HEAP16, HEAPU16, HEAP32, HEAPU32, HEAPF32, HEAPF64;

function updateGlobalBufferAndViews(buf) {
    buffer = buf;
    yinModule["HEAP8"] = HEAP8 = new Int8Array(buf);
    yinModule["HEAP16"] = HEAP16 = new Int16Array(buf);
    yinModule["HEAP32"] = HEAP32 = new Int32Array(buf);
    yinModule["HEAPU8"] = HEAPU8 = new Uint8Array(buf);
    yinModule["HEAPU16"] = HEAPU16 = new Uint16Array(buf);
    yinModule["HEAPU32"] = HEAPU32 = new Uint32Array(buf);
    yinModule["HEAPF32"] = HEAPF32 = new Float32Array(buf);
    yinModule["HEAPF64"] = HEAPF64 = new Float64Array(buf)
}
var INITIAL_MEMORY = yinModule["INITIAL_MEMORY"] || 16777216;
var wasmTable;
var __ATPRERUN__ = [];
var __ATINIT__ = [];
var __ATPOSTRUN__ = [];
var runtimeInitialized = false;

function keepRuntimeAlive() {
    return noExitRuntime
}

function preRun() {
    if (yinModule["preRun"]) {
        if (typeof yinModule["preRun"] == "function") yinModule["preRun"] = [yinModule["preRun"]];
        while (yinModule["preRun"].length) {
            addOnPreRun(yinModule["preRun"].shift())
        }
    }
    callRuntimeCallbacks(__ATPRERUN__)
}

function initRuntime() {
    runtimeInitialized = true;
    callRuntimeCallbacks(__ATINIT__)
}

function postRun() {
    if (yinModule["postRun"]) {
        if (typeof yinModule["postRun"] == "function") yinModule["postRun"] = [yinModule["postRun"]];
        while (yinModule["postRun"].length) {
            addOnPostRun(yinModule["postRun"].shift())
        }
    }
    callRuntimeCallbacks(__ATPOSTRUN__)
}

function addOnPreRun(cb) {
    __ATPRERUN__.unshift(cb)
}

function addOnInit(cb) {
    __ATINIT__.unshift(cb)
}

function addOnPostRun(cb) {
    __ATPOSTRUN__.unshift(cb)
}
var runDependencies = 0;
var runDependencyWatcher = null;
var dependenciesFulfilled = null;

function addRunDependency(id) {
    runDependencies++;
    if (yinModule["monitorRunDependencies"]) {
        yinModule["monitorRunDependencies"](runDependencies)
    }
}

function removeRunDependency(id) {
    runDependencies--;
    if (yinModule["monitorRunDependencies"]) {
        yinModule["monitorRunDependencies"](runDependencies)
    }
    if (runDependencies == 0) {
        if (runDependencyWatcher !== null) {
            clearInterval(runDependencyWatcher);
            runDependencyWatcher = null
        }
        if (dependenciesFulfilled) {
            var callback = dependenciesFulfilled;
            dependenciesFulfilled = null;
            callback()
        }
    }
}

function abort(what) {
    if (yinModule["onAbort"]) {
        yinModule["onAbort"](what)
    }
    what = "Aborted(" + what + ")";
    err(what);
    ABORT = true;
    EXITSTATUS = 1;
    what += ". Build with -sASSERTIONS for more info.";
    var e = new WebAssembly.RuntimeError(what);
    throw e
}
var dataURIPrefix = "data:application/octet-stream;base64,";

function isDataURI(filename) {
    return filename.startsWith(dataURIPrefix)
}

function isFileURI(filename) {
    return filename.startsWith("file://")
}
var wasmBinaryFile;
wasmBinaryFile = "CFunctions.wasm";
if (!isDataURI(wasmBinaryFile)) {
    wasmBinaryFile = locateFile(wasmBinaryFile)
}

function getBinary(file) {
    try {
        if (file == wasmBinaryFile && wasmBinary) {
            return new Uint8Array(wasmBinary)
        }
        if (readBinary) {
            return readBinary(file)
        }
        throw "both async and sync fetching of the wasm failed"
    } catch (err) {
        abort(err)
    }
}

function getBinaryPromise() {
    if (!wasmBinary && (ENVIRONMENT_IS_WEB || ENVIRONMENT_IS_WORKER)) {
        if (typeof fetch == "function" && !isFileURI(wasmBinaryFile)) {
            return fetch(wasmBinaryFile, {
                credentials: "same-origin"
            }).then(function(response) {
                if (!response["ok"]) {
                    throw "failed to load wasm binary file at '" + wasmBinaryFile + "'"
                }
                return response["arrayBuffer"]()
            }).catch(function() {
                return getBinary(wasmBinaryFile)
            })
        } else {
            if (readAsync) {
                return new Promise(function(resolve, reject) {
                    readAsync(wasmBinaryFile, function(response) {
                        resolve(new Uint8Array(response))
                    }, reject)
                })
            }
        }
    }
    return Promise.resolve().then(function() {
        return getBinary(wasmBinaryFile)
    })
}

function createWasm() {
    var info = {
        "a": asmLibraryArg
    };

    function receiveInstance(instance, module) {
        var exports = instance.exports;
        yinModule["asm"] = exports;
        wasmMemory = yinModule["asm"]["b"];
        updateGlobalBufferAndViews(wasmMemory.buffer);
        wasmTable = yinModule["asm"]["e"];
        addOnInit(yinModule["asm"]["c"]);
        removeRunDependency("wasm-instantiate")
    }
    addRunDependency("wasm-instantiate");

    function receiveInstantiationResult(result) {
        receiveInstance(result["instance"])
    }

    function instantiateArrayBuffer(receiver) {
        return getBinaryPromise().then(function(binary) {
            return WebAssembly.instantiate(binary, info)
        }).then(function(instance) {
            return instance
        }).then(receiver, function(reason) {
            err("failed to asynchronously prepare wasm: " + reason);
            abort(reason)
        })
    }

    function instantiateAsync() {
        if (!wasmBinary && typeof WebAssembly.instantiateStreaming == "function" && !isDataURI(
            wasmBinaryFile) && !isFileURI(wasmBinaryFile) && !ENVIRONMENT_IS_NODE && typeof fetch ==
            "function") {
            return fetch(wasmBinaryFile, {
                credentials: "same-origin"
            }).then(function(response) {
                var result = WebAssembly.instantiateStreaming(response, info);
                return result.then(receiveInstantiationResult, function(reason) {
                    err("wasm streaming compile failed: " + reason);
                    err("falling back to ArrayBuffer instantiation");
                    return instantiateArrayBuffer(receiveInstantiationResult)
                })
            })
        } else {
            return instantiateArrayBuffer(receiveInstantiationResult)
        }
    }
    if (yinModule["instantiateWasm"]) {
        try {
            var exports = yinModule["instantiateWasm"](info, receiveInstance);
            return exports
        } catch (e) {
            err("Module.instantiateWasm callback failed with error: " + e);
            return false
        }
    }
    instantiateAsync();
    return {}
}

function ExitStatus(status) {
    this.name = "ExitStatus";
    this.message = "Program terminated with exit(" + status + ")";
    this.status = status
}

function callRuntimeCallbacks(callbacks) {
    while (callbacks.length > 0) {
        callbacks.shift()(yinModule)
    }
}

function getHeapMax() {
    return 2147483648
}

function emscripten_realloc_buffer(size) {
    try {
        wasmMemory.grow(size - buffer.byteLength + 65535 >>> 16);
        updateGlobalBufferAndViews(wasmMemory.buffer);
        return 1
    } catch (e) {}
}

function _emscripten_resize_heap(requestedSize) {
    var oldSize = HEAPU8.length;
    requestedSize = requestedSize >>> 0;
    var maxHeapSize = getHeapMax();
    if (requestedSize > maxHeapSize) {
        return false
    }
    let alignUp = (x, multiple) => x + (multiple - x % multiple) % multiple;
    for (var cutDown = 1; cutDown <= 4; cutDown *= 2) {
        var overGrownHeapSize = oldSize * (1 + .2 / cutDown);
        overGrownHeapSize = Math.min(overGrownHeapSize, requestedSize + 100663296);
        var newSize = Math.min(maxHeapSize, alignUp(Math.max(requestedSize, overGrownHeapSize), 65536));
        var replacement = emscripten_realloc_buffer(newSize);
        if (replacement) {
            return true
        }
    }
    return false
}

function getCFunc(ident) {
    var func = yinModule["_" + ident];
    return func
}

function writeArrayToMemory(array, buffer) {
    HEAP8.set(array, buffer)
}

function ccall(ident, returnType, argTypes, args, opts) {
    var toC = {
        "string": str => {
            var ret = 0;
            if (str !== null && str !== undefined && str !== 0) {
                var len = (str.length << 2) + 1;
                ret = stackAlloc(len);
                stringToUTF8(str, ret, len)
            }
            return ret
        },
        "array": arr => {
            var ret = stackAlloc(arr.length);
            writeArrayToMemory(arr, ret);
            return ret
        }
    };

    function convertReturnValue(ret) {
        if (returnType === "string") {
            return UTF8ToString(ret)
        }
        if (returnType === "boolean") return Boolean(ret);
        return ret
    }
    var func = getCFunc(ident);
    var cArgs = [];
    var stack = 0;
    if (args) {
        for (var i = 0; i < args.length; i++) {
            var converter = toC[argTypes[i]];
            if (converter) {
                if (stack === 0) stack = stackSave();
                cArgs[i] = converter(args[i])
            } else {
                cArgs[i] = args[i]
            }
        }
    }
    var ret = func.apply(null, cArgs);

    function onDone(ret) {
        if (stack !== 0) stackRestore(stack);
        return convertReturnValue(ret)
    }
    ret = onDone(ret);
    return ret
}
var asmLibraryArg = {
    "a": _emscripten_resize_heap
};
var asm = createWasm();
var ___wasm_call_ctors = yinModule["___wasm_call_ctors"] = function() {
    return (___wasm_call_ctors = yinModule["___wasm_call_ctors"] = yinModule["asm"]["c"]).apply(null, arguments)
};
var _C_getPitch = yinModule["_C_getPitch"] = function() {
    return (_C_getPitch = yinModule["_C_getPitch"] = yinModule["asm"]["d"]).apply(null, arguments)
};
var _mallocMemory = yinModule["_mallocMemory"] = function() {
    return (_mallocMemory = yinModule["_mallocMemory"] = yinModule["asm"]["f"]).apply(null, arguments)
};
var _freeMemory = yinModule["_freeMemory"] = function() {
    return (_freeMemory = yinModule["_freeMemory"] = yinModule["asm"]["g"]).apply(null, arguments)
};
var stackSave = yinModule["stackSave"] = function() {
    return (stackSave = yinModule["stackSave"] = yinModule["asm"]["h"]).apply(null, arguments)
};
var stackRestore = yinModule["stackRestore"] = function() {
    return (stackRestore = yinModule["stackRestore"] = yinModule["asm"]["i"]).apply(null, arguments)
};
var stackAlloc = yinModule["stackAlloc"] = function() {
    return (stackAlloc = yinModule["stackAlloc"] = yinModule["asm"]["j"]).apply(null, arguments)
};
yinModule["ccall"] = ccall;
var calledRun;
dependenciesFulfilled = function runCaller() {
    if (!calledRun) run();
    if (!calledRun) dependenciesFulfilled = runCaller
};

function run(args) {
    args = args || arguments_;
    if (runDependencies > 0) {
        return
    }
    preRun();
    if (runDependencies > 0) {
        return
    }

    function doRun() {
        if (calledRun) return;
        calledRun = true;
        yinModule["calledRun"] = true;
        if (ABORT) return;
        initRuntime();
        if (yinModule["onRuntimeInitialized"]) yinModule["onRuntimeInitialized"]();
        postRun()
    }
    if (yinModule["setStatus"]) {
        yinModule["setStatus"]("Running...");
        setTimeout(function() {
            setTimeout(function() {
                yinModule["setStatus"]("")
            }, 1);
            doRun()
        }, 1)
    } else {
        doRun()
    }
}
if (yinModule["preInit"]) {
    if (typeof yinModule["preInit"] == "function") yinModule["preInit"] = [yinModule["preInit"]];
    while (yinModule["preInit"].length > 0) {
        yinModule["preInit"].pop()()
    }
}
run();