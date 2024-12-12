from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from qiskit import Aer
from qiskit.algorithms import QAOA
from qiskit.optimization import QuadraticProgram
from qiskit.optimization.converters import QuadraticProgramToQubo

app = FastAPI(title="Simple Quantum-Inspired Optimization API")

class MaxCutRequest(BaseModel):
    graph: list[list[int]]
    p: int = 1

@app.post("/max_cut")
async def max_cut(request: MaxCutRequest):
    try:
        graph = np.array(request.graph)
        num_nodes = len(graph)

        qp = QuadraticProgram()
        for i in range(num_nodes):
            qp.binary_var(f'x_{i}')

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if graph[i, j] == 1:
                    qp.objective.linear[f'x_{i}'] += 1
                    qp.objective.linear[f'x_{j}'] += 1
                    qp.objective.quadratic[f'x_{i}', f'x_{j}'] -= 2

        qubo = QuadraticProgramToQubo().convert(qp)

        backend = Aer.get_backend('qasm_simulator')
        qaoa = QAOA(quantum_instance=backend, p=request.p)
        result = qaoa.compute_minimum_eigenvalue(qubo)

        optimal_bitstring = "".join(map(str, map(int, result.optimal_bitstring)))
        optimal_value = result.optimal_value

        return {"optimal_bitstring": optimal_bitstring, "optimal_value": optimal_value}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))