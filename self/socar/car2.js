function permutator (arr, n) {
    let results = []
    if (n === 1) return arr.map((v) => [v])

    arr.forEach((fixed, idx, org) => {
        const rest = [...org.slice(0, idx), ...org.slice(idx+1)]
        const permutations = permutator(rest, n-1)
        const tmp = permutations.map((perm) => [fixed, ...perm])
        results.push(...tmp)
    })
    return results
}


function count_swap(arr) {
    let l = arr.length
    let p = []

    for (let i = 0; i < l; i++){
        p.push([arr[i],i]);
    }

    p.sort((x,y) => x[0] - y[0])

    let v = new Array(l).fill(false)
    let cnt = 0

    for (let i = 0; i < l; i++){
        if (v[i] || p[i][1] === i){
            continue
        }

        let size = 0
        let j = i
        while (!v[j]){
            v[j] = true
            j = p[j][1]
            size++
        }
        cnt += size - 1
    }
    return cnt
}

function get_minimum(a, b) {
    const l = a.length
    let mp = new Map();

    for (let i = 0; i < l; i++){
        mp.set(b[i],i)
    }

    for (let i = 0; i < l; i++ ){
        b[i] = mp.get(a[i])
    }

    return count_swap(b)
}


function solution(numbers, K) {
    var answer = Infinity;
    const l = numbers.length
    const res = permutator(numbers, l)

    const filtered = res.filter((arr) => {
        for (let i = 0; i < l-1; i++){
            if (Math.abs(arr[i]-arr[i+1]) > K){
                return false
            } 
        }
        return true
    })

    if (filtered.length === 0) {
        return -1
    }

    filtered.forEach(arr => {
        const cnt = get_minimum(numbers, arr)
        answer = Math.min(answer, cnt)
    })

    return answer;
}