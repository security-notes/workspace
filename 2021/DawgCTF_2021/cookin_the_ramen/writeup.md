# Writeup

見た目はモールス信号なので、CyberChefで解読してみる。

サジェストに従うと、モールス信号 ⇒ Base32 ⇒ Base64 ⇒ Base58 でフラグが得られた。

* [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Line%20feed')From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9%2B/%3D',true)From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',false)&input=IC4tLS0gLi4uLSAuLi4tIC4gLi4uLi0gLi4uLSAuLi4gLi4tLS0gLi4gLi0uIC4tLSAtLS4gLS4tLiAuLS0gLS4tIC0uLS0gLS4gLS4uLiAuLi0tLSAuLi0uIC0uLS4gLi4uLSAuLi4tLSAuLi0gLS0uIC4tLS0gLi4uIC4uLSAuLiAtLS4uIC0uLS4gLi4uLiAtLSAuLi4tIC0uLSAuIC4uLSAtLSAtIC4gLS4gLi4uLSAtLiAuLi0uIC0tLSAtLi0tIC0tLi4gLSAuLS4uIC4tLS0gLS0uLiAtLS4gLS0uIC4uLi0tIC4uLiAtLi0uIC0uLSAuLi4uLiAuLS0tIC4uLSAtLS0gLS4gLS4tIC0uLi0gLS4tIC0tLi4gLS4tIC4uLi0gLi4tIC4tLSAtIC0uLiAuLS0tIC0uLi4gLi4uLiAuLi0uIC0tLiAtLS4uIC0uLSAtLi4tIC4uIC0tLi4gLi0tIC4uLi0gLi4uIC0tIC4uLi0tIC0tLi0gLS0uIC4uLS4gLi4uIC4tLSAtLS0gLi0tLiAuLS0tIC4uLi4u)

<!-- DawgCTF{0k@y_r3al_b@by's_f1r5t} -->
