import api from "./api"
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import "./Auth.css"

function Cadastro() {
    const navigate = useNavigate()
    const [nome, setNome] = useState('')
    const [email, setEmail] = useState('')
    const [senha, setSenha] = useState('')

    async function enviar() {
        try {
            // 1. Faz o cadastro
            const responseCadastro = await api.post('/cadastro', null, {
                params: { nome, email, senha }
            });

            if (responseCadastro.data) {
                // 2. O cadastro deu certo? Faz o login silencioso logo em seguida!
                const responseLogin = await api.get('/login', {
                    params: { email, senha }
                });

                // 3. Pega o ID e o Nome, salva no navegador e vai pra Home!
                if (responseLogin.data && responseLogin.data.id) {
                    localStorage.setItem('idUsuario', responseLogin.data.id);
                    localStorage.setItem('nome', responseLogin.data.nome);

                    alert("Conta criada com sucesso!");
                    navigate('/'); // Agora sim vai pra tela principal e fica!
                }
            }
        } catch (error) {
            alert("Erro ao cadastrar. Verifique se o email já existe ou tente novamente.");
        }
    }

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h1 className="auth-titulo">MyTasks</h1>
                <p className="auth-subtitulo">Crie sua conta</p>
                <div className="auth-campo">
                    <label>Nome</label>
                    <input value={nome} onChange={e => setNome(e.target.value)} type="text" placeholder="Seu nome" />
                </div>
                <div className="auth-campo">
                    <label>Email</label>
                    <input value={email} onChange={e => setEmail(e.target.value)} type="email" placeholder="seu@email.com" />
                </div>
                <div className="auth-campo">
                    <label>Senha</label>
                    <input value={senha} onChange={e => setSenha(e.target.value)} type="password" placeholder="••••••••" />
                </div>
                <button className="auth-btn" onClick={enviar}>Cadastrar</button>
                <p className="auth-link" onClick={() => navigate('/login')}>Já tem conta? Entre</p>
            </div>
        </div>
    )
}

export default Cadastro 