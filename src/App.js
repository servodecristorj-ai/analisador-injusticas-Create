import React, { useState } from 'react';

function App() {
  const [salarioMinimo] = useState(1621);
  const [valorParlamentar, setValorParlamentar] = useState(262037.79);
  const [nomeParlamentar, setNomeParlamentar] = useState('Deputado Federal - Teto de Gastos');

  const diferenca = valorParlamentar - salarioMinimo;
  const multiplicador = (valorParlamentar / salarioMinimo).toFixed(0);
  const percentual = ((diferenca / salarioMinimo) * 100).toFixed(0);

  const aplicarCenario = (valor, nome) => {
    setValorParlamentar(valor);
    setNomeParlamentar(nome);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-4">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold mb-2">⚖️ Analisador de Injustiças</h1>
          <p className="text-gray-400">O Valor de uma Transição</p>
        </div>

        <div className="bg-red-900/30 border border-red-500 rounded-lg p-6 mb-6">
          <h2 className="text-2xl font-bold text-red-400 mb-4">POSSÍVEL INJUSTIÇA DETECTADA</h2>
          <p className="text-lg mb-2">Cenário: <span className="font-bold">{nomeParlamentar}</span></p>
          <div className="grid grid-cols-2 gap-4 mt-4">
            <div>
              <p className="text-gray-400">Custo Parlamentar</p>
              <p className="text-2xl font-bold">R$ {valorParlamentar.toLocaleString('pt-BR')}</p>
            </div>
            <div>
              <p className="text-gray-400">Salário Mínimo</p>
              <p className="text-2xl font-bold">R$ {salarioMinimo.toLocaleString('pt-BR')}</p>
            </div>
          </div>
          <div className="mt-6 bg-black/40 p-4 rounded">
            <p className="text-xl">Diferença: <span className="text-red-400 font-bold">R$ {diferenca.toLocaleString('pt-BR')}</span></p>
            <p className="text-xl">Multiplicador: <span className="text-red-400 font-bold">{multiplicador}x maior</span></p>
            <p className="text-xl">Percentual: <span className="text-red-400 font-bold">{percentual}% acima</span></p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <button
            onClick={() => aplicarCenario(262037.79, 'Deputado Federal - Teto de Gastos')}
            className="bg-blue-600 hover:bg-blue-700 p-4 rounded-lg"
          >
            <p className="font-bold">Metodologia 1</p>
            <p className="text-sm">Deputado Federal</p>
            <p className="text-xl mt-2">R$ 262.037,79</p>
          </button>

          <button
            onClick={() => aplicarCenario(485000, 'Transição Governo RJ - Estimativa')}
            className="bg-purple-600 hover:bg-purple-700 p-4 rounded-lg"
          >
            <p className="font-bold">Metodologia 2</p>
            <p className="text-sm">Transição RJ</p>
            <p className="text-xl mt-2">R$ 485.000,00</p>
          </button>
        </div>

        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>Dados baseados no Portal da Transparência RJ e Câmara dos Deputados</p>
          <p>Base 2026 - Salário Mínimo: R$ 1.621,00</p>
        </div>
      </div>
    </div>
  );
}

export default App;
