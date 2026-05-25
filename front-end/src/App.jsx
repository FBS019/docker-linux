import { useState, useEffect } from 'react'
import api from '../api'
import './App.css'

function App() {
  const [tarefas, setTarefas] = useState([])
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

  async function atualizar() {

  }

  useEffect(() => {
    getTarefas()
  }, [])

  return (
    <div className="container">
      
      <header className="header">
        <h1 className="titulo">MyTasks</h1>
        <div className="header-acoes">
          <button className="btn-adicionar">+ Nova Tarefa</button>
          <button className="btn-pesquisar">🔍</button>
        </div>
      </header>

      <div className="lista">
        {tarefas.map(tarefa => (
          <div key={tarefa.id} className="card">
            <div className="card-conteudo">
              <p className="card-titulo">{tarefa.titulo}</p>
              <p className="card-descricao">{tarefa.descricao}</p>
              <span className={tarefa.status ? 'badge-concluida' : 'badge-pendente'}>
                {tarefa.status ? 'Concluída' : 'Pendente'}
              </span>
            </div>
            <div className="card-acoes">
              <button className="btn-editar" onClick={() => atualizar(tarefa.id)} title="Editar">✏️</button>
              <button className="btn-deletar" onClick={() => deletar(tarefa.id)} title="Deletar">🗑️</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App