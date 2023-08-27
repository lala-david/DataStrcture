function countdown(number) {
    if (number <= 0) {
        console.log("끝!");
    } else {
        console.log(number);
        countdown(number - 1);
    }
}

countdown(10);
