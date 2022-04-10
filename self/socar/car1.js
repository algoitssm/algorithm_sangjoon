function solution(n, k, roads) {
    var answer = new Set();

    let graph = {}

    roads.forEach(([a,b,d]) => {
        tmp1 = graph[a] ? graph[a] : []
        tmp2 = graph[b] ? graph[b] : []
        graph[a] = [...tmp1, [b.toString(),d]]
        graph[b] = [...tmp2, [a.toString(),d]]
    })

    let dq = [["0",0]]

    while (dq.length !== 0){
        const [s, t] = dq.shift()
        graph[s].forEach(([e, d]) => {
            if (t+d === k){
                answer.add(parseInt(e))
            }
            else if (t+d <= k){
                dq.push([e, t+d])
            }
        })
    }

    answer = !!answer.size ?  Array.from(answer).sort() : [-1]
    return answer;
}

function bisect_right(arr, target, s, e) {

    if(s >= e){ 
        return s
    }

    const m = Math.floor((s + e)/2)

    if(target < arr[m][1]){
        return bisect_right(arr, target, s, m)
    }else{
        return bisect_right(arr, target, m+1, e)        
    }
}

function solution(n, k, roads) {
    var answer = new Set();
    let graph = new Map()

    roads.forEach(([a,b,d]) => {
        tmp1 = !graph.get(a) ? [] : graph.get(a)
        tmp2 = !graph.get(b) ? [] : graph.get(b)
        graph.set(a,[...tmp1, [b,d]]) 
        graph.set(b,[...tmp2, [a,d]])
    })

    graph.forEach((a)=> {
        a.sort((x,y) => x[1] - y[1])
    })

    let dq = [[0,0]]
    let v = Array(n).fill([0,0])

    while (dq.length !== 0){
        const [s, t] = dq.shift()

        const tmp = graph.get(s)
        const idx = bisect_right(tmp, k-t, 0, tmp.length)

        for (let i = 0; i < idx; i++){
            const [e, d] = tmp[i]
            if (t+d === k){
                answer.add(e)
            }

            else if (t+d < k){
                dq.push([e, t+d])
            }
        }

    }

    answer = !answer.size ? [-1] : Array.from(answer).sort()

    return answer;
}