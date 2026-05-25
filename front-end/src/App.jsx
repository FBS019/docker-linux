import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api'
import './App.css'

function App() {
  const navigate = useNavigate()
  const [tarefas, setTarefas] = useState([])
  const [busca, setBusca] = useState('')
  const [modalAberto, setModalAberto] = useState(false)
  const [tarefaEditando, setTarefaEditando] = useState(null)
  const [form, setForm] = useState({ titulo: '', descricao: '', status: 'Pendente' })

  const idUsuario = localStorage.getItem('idUsuario')

  async function getTarefas() {
    const response = await api.get('/tarefas', {
      params: { idUsuario }
    })
    setTarefas(response.data)
  }

  async function deletar(idTarefa) {
    await api.delete(`/tarefas/deletar/${idTarefa}`)
    getTarefas()
  }

  async function salvar() {
    if (tarefaEditando) {
      await api.put(`/tarefas/atualizar/${tarefaEditando.id}`, form)
    } else {
      await api.post('/tarefas/criar', { ...form, idUsuario })
    }
    setModalAberto(false)
    getTarefas()
  }

  function abrirEditar(tarefa) {
    setTarefaEditando(tarefa)
    setForm({ titulo: tarefa.titulo, descricao: tarefa.descricao, status: tarefa.status })
    setModalAberto(true)
  }

  function abrirNovo() {
    setTarefaEditando(null)
    setForm({ titulo: '', descricao: '', status: 'Pendente' })
    setModalAberto(true)
  }

  function deslogar() {
    localStorage.removeItem('idUsuario')
    navigate('/login')
  }

  useEffect(() => {
    if (!idUsuario) {
      navigate('/login')
    } else {
      getTarefas()
    }
  }, [idUsuario, navigate])

  const tarefasFiltradas = tarefas.filter(tarefa => 
    tarefa.titulo.toLowerCase().includes(busca.toLowerCase()) || 
    tarefa.descricao.toLowerCase().includes(busca.toLowerCase())
  )

  return (
    <div className="container">
      <header className="header">
        <h1 className="titulo">MyTasks</h1>
        <div className="header-acoes">
          <input 
            type="text" 
            placeholder="🔍 Pesquisar tarefa..." 
            className="input-pesquisa"
            value={busca}
            onChange={(e) => setBusca(e.target.value)}
          />
          <button className="btn-adicionar" onClick={abrirNovo}>+ Nova Tarefa</button>
          <button className="btn-sair" onClick={deslogar}>Sair</button>
        </div>
      </header>

      <div className="lista">
        {tarefasFiltradas.map(tarefa => (
          <div key={tarefa.id} className="card">
            <div className="card-conteudo">
              <p className="card-titulo">{tarefa.titulo}</p>
              <p className="card-descricao">{tarefa.descricao}</p>
              <span className={tarefa.status === 'Concluída' ? 'badge-concluida' : 'badge-pendente'}>
                {tarefa.status}
              </span>
            </div>
            <div className="card-acoes">
              <button className="btn-editar" onClick={() => abrirEditar(tarefa)} title="Editar">✏️</button>
              <button className="btn-deletar" onClick={() => deletar(tarefa.id)} title="Deletar">🗑️</button>
            </div>
          </div>
        ))}
      </div>

      {modalAberto && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>{tarefaEditando ? 'Editar Tarefa' : 'Nova Tarefa'}</h2>
            <input
              className="input"
              placeholder="Título"
              value={form.titulo}
              onChange={e => setForm({ ...form, titulo: e.target.value })}
            />
            <textarea
              className="input"
              placeholder="Descrição"
              value={form.descricao}
              onChange={e => setForm({ ...form, descricao: e.target.value })}
            />
            <select
              className="input"
              value={form.status}
              onChange={e => setForm({ ...form, status: e.target.value })}
            >
              <option value="Pendente">Pendente</option>
              <option value="Concluída">Concluída</option>
            </select>
            <div className="modal-acoes">
              <button className="btn-cancelar" onClick={() => setModalAberto(false)}>Cancelar</button>
              <button className="btn-salvar" onClick={salvar}>Salvar</button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
