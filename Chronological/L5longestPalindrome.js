const longestPalindrome = (str) => {
    let n = str.length
    let table = Array.from({ length: n }, () => Array(n).fill(false))

    let maxLen = 1
    let longPalin = str[0]

    for (let i = 0; i < n; i++) {
        table[i][i] = true
    }
    for (let i = 0; i < n - 1; i++) {
        if (str[i] === str[i + 1]) {
            table[i][i + 1] = true
            maxLen = 2
            longPalin = str.slice(i, i + 2)
        }
    }

    for (let length = 3; length <= n; length++) {
        for (let start = 0; start <= n - length; start++) {
            let end = start + length - 1
            if (str[start] === str[end] && table[start + 1][end - 1]) {
                table[start][end] = true
                if (length > maxLen) {
                    maxLen = length
                    longPalin = str.slice(start, end + 1)
                }
            }
        }
    }

    return longPalin
}
console.log(longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"))