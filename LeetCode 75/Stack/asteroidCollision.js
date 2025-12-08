const asteroidCollision = (asteroids) => {
    const survivors = []
    for (let i = 0; i < asteroids.length; i++) {
        const num = asteroids[i]
        
        if (num >= 0) {
            survivors.push(num)
        } else {
            if (survivors.at(-1) < 0) {
                survivors.push(num)
                continue
            }
            while (true) {
                if (survivors.at(-1) < 0) {
                    survivors.push(num)
                    break
                }
                if (survivors.length === 0) {
                    survivors.push(num)
                    break
                }
                if (Math.abs(num) > Math.abs(survivors.at(-1))) {
                    survivors.pop()
                } else if (Math.abs(num) === Math.abs(survivors.at(-1))) {
                    survivors.pop()
                    break
                } else {
                    break
                }
            }
        }
    }
    return survivors
}

console.log(asteroidCollision([-2,-1,1,-2]))