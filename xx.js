function test() {
    let arr = [3, 4, 5, 6]

    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * 3
    }

    console.log(arr) // [9, 12, 15, 18]

    let arr1 = [3, 4, 5, 6]

    let modifiedArr = arr1.map(function (element) {
        if (element === 3) return element * 3
    })

    console.log(modifiedArr)

    let arr2 = [2, 3, 5, 7]

    arr2.map(function (element, index, array) {
        console.log(element)
        console.log(index)
        console.log(array)
        return element
    }, 80)
}

const wait = async (ms) => {
    setTimeout(() => {
        console.log("wating " + ms + " s")
    }, ms * 1000)
}

// async function main() {
//     console.log(2)
//     await wait(1)
//     console.log(4)
// }

// console.log(1)
// let what = main()
// console.log(3)
// console.log(what)

// async function asyncFn(str) {
//     setTimeout(() => {
//         console.log("最后执行")
//     }, 3000)
//     console.log("开始")
//     fibonacci(40) // 耗时操作, 阻塞了
//     console.log(1)
//     return str + "加工"
// }
// let asyncRet = asyncFn("I am a Async Function")
// asyncRet.then((str) => {
//     console.log(str)
// })
// console.log("本来在最后面, 却在最前面")

async function read_file() {
    console.log("initial read_file sleep(2.1)")
    await wait(2)
    console.log("read_file 1/2 wait(2)")
    await wait(0.1)
    console.log("read_file 2/2 wait(0.1)")
    return "file result"
}

async function read_api() {
    console.log("initial read_api wait(2)")
    await wait(2)
    console.log("read_api whole wait(2)")
    return "api result"
}

async function read_db() {
    console.log("initial read_db wait(3)")
    await wait(3)
    console.log("read_db whole wait(3)")
    return "db result"
}

read_file()
console.log("does not block")
read_api()
console.log("the second time, won't block")
read_db()
// initial read_file sleep(2.1)
// does not block
// initial read_api wait(2)
// the second time, won't block
// initial read_db wait(3)
// read_file 1/2 wait(2)
// read_api whole wait(2)
// read_db whole wait(3)
// read_file 2/2 wait(0.1)
// wating: 0.1
// wating: 2
// wating: 2
// wating: 3


// foreach

var myObject = { name: "myObject" }
console.log(this)

[1, 2].forEach((item) => {
  console.log(item) // 1, 2
  console.log(this === myObject, this) // false  Window {}
}, myObject)

[1, 2].forEach(function (item) {
  console.log(item) // 1, 2
  console.log(this === myObject, this) // true  {name: "myObject"}
}, myObject)

[1, 2].forEach(function (item) {
  console.log(item) // 1, 2
  console.log(this === myObject, this) // true  {name: "myObject"}
})
