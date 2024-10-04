import "./loguin.css"
import { useState } from "react"

export function loguinreact (){
    const [nombre, setnombre] = useState ("")
    const [contraseña, setContraseña] = useState("")
    
    return (
        <section>
            <h1>loguin</h1>

            <form class ="loguin">
                <input 
                    type="text"
                    value={nombre}
                    onChange={e => setnombre(e.target.value)}
                />

                <input 
                    type="pasword"
                    value={contraseña}
                    onChange={e => setContraseña(e.target.value)}
                />
                <button>iniciar sesion</button>
            </form>

        </section>
    )
}