import api from "./api"
import { useState } from "react"
import "./Auth.css"

function Login() {
    const navigate = useNavigate()
    const [email, setEmail] = useState('')
    const [senha, setSenha] = useState('')

    async function enviar() {
        const response = await api.get('/login', {
            params: { email, senha }
        })
        if (response.data) {
            localStorage.setItem('idUsuario', response.data)
            navigate('/')
        }
    }

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h1 className="auth-titulo">MyTasks</h1>
                <p className="auth-subtitulo">Entre na sua conta</p>
                <div className="auth-campo">
                    <label>Email</label>
                    <input value={email} onChange={e => setEmail(e.target.value)} type="email" placeholder="seu@email.com" />
                </div>
                <div className="auth-campo">
                    <label>Senha</label>
                    <input value={senha} onChange={e => setSenha(e.target.value)} type="password" placeholder="••••••••" />
                </div>
                <button className="auth-btn" onClick={enviar}>Entrar</button>
                <p className="auth-link" onClick={() => navigate('/cadastro')}>Não tem conta? Cadastre-se</p>
            </div>
        </div>
    )
}

export default Login 