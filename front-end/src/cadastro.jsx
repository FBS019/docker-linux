import api from "./api"
import { useState } from "react"
import {useNavigate} from "react-router-dom"
import "./Auth.css"

function Cadastro(){
    const navigate = useNavigate()
    const [nome,setNome] = useState('')
    const [email,setEmail] = useState('')
    const [senha,setSenha] = useState('')

    async function enviar(){
        const response = await api.post('/cadastro', {nome,email,senha} )
        if(response.data){
            localStorage.setItem('idUsuario',response.data)
            navigate('/')
        }
    }

    return(
        <div className="auth-container">
            <div className="auth-card">
                <h1 className="auth-titulo">MyTasks</h1>
                <p className="auth-subtitulo">Crie sua conta</p>
                <div className="auth-campo">
                    <label>Nome</label>
                    <input value={nome} onChange={e => setNome(e.target.value)} type="text" placeholder="Seu nome"/>
                </div>
                <div className="auth-campo">
                    <label>Email</label>
                    <input value={email} onChange={e => setEmail(e.target.value)} type="email" placeholder="seu@email.com"/>
                </div>
                <div className="auth-campo">
                    <label>Senha</label>
                    <input value={senha} onChange={e => setSenha(e.target.value)} type="password" placeholder="••••••••"/>
                </div>
                <button className="auth-btn" onClick={enviar}>Cadastrar</button>
                <p className="auth-link" onClick={() => navigate('/login')}>Já tem conta? Entre</p>
            </div>
        </div>
    )
}

export default Cadastro 