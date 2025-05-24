var memeAddresses = [
    "https://media3.giphy.com/media/Dg4TxjYikCpiGd7tYs/200w.gif?cid=6c09b9526hcjygmd8vc0o55ecba25w8sjn5z3b1nk38csw9z&ep=v1_gifs_search&rid=200w.gif&ct=g",
    "https://i.makeagif.com/media/1-12-2024/DdRS1W.gif"
]

var bodyTemp = ""

shiftdown = false

function main() {
    console.log("The Javascript is running!!")
    //KeyDOWN
    document.addEventListener("keydown", (event) => {
        console.log("Key down:  " + event.key)
        if (event.key === "Shift"){
            if (shiftdown == false) {
                shiftdown = true
                //console.log("SHIFT")
                const e = document.getElementById("htmlBody");
                if (bodyTemp == "") {
                    bodyTemp = e.innerHTML;
                }
                max = Math.floor(Math.random() * (memeAddresses.length))
                console.log(max)
                document.getElementById("htmlBody").innerHTML = '<img src="' + memeAddresses[max] + '" alt="Funny meme goes here." class="memes">'
            }
        }
    });
    //KeyUP
    document.addEventListener("keyup", (event) => {
        console.log("Key up:  " + event.key)
        if (event.key === "Shift"){
            shiftdown = false
            document.getElementById("htmlBody").innerHTML = bodyTemp
        }
    });
}


main();