import tkinter as tk
import os
import time

class JanelaVigia:
    def __init__(self, timeout=60):
        self.root = tk.Tk()
        self.root.title("Alerta de Inatividade")
        self.root.attributes("-topmost", True)  # Sempre na frente
        self.timeout = timeout
        self.clicou_sim = False

        # Configuração da Janela
        self.label = tk.Label(self.root, text=f"Você ainda está acordado?\nDesligando em {self.timeout}s", 
                              font=("Arial", 12), padx=20, pady=20)
        self.label.pack()

        self.btn_sim = tk.Button(self.root, text="SIM, ESTOU ACORDADO!", 
                                 command=self.confirmar, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.btn_sim.pack(pady=10)

        # Inicia a contagem regressiva
        self.atualizar_timer()
        self.root.mainloop()

    def confirmar(self):
        self.clicou_sim = True
        self.root.destroy()

    def atualizar_timer(self):
        if self.timeout > 0:
            self.timeout -= 1
            self.label.config(text=f"Você ainda está acordado?\nDesligando em {self.timeout}s")
            self.root.after(1000, self.atualizar_timer) # Chama essa função de novo em 1s
        else:
            self.root.destroy() # Tempo acabou, fecha a janela

def executar_monitor():
    print("Monitor ativo. Verificação a cada 2 horas.")
    while True:
        time.sleep(7200) # 2 horas
        
        # Abre a janela e espera 60 segundos pela resposta
        app = JanelaVigia(timeout=60)
        
        if not app.clicou_sim:
            print("Tempo esgotado ou resposta negativa. Desligando...")
            os.system("shutdown /s /t 10") # Desliga em 10 segundos
            break
        else:
            print("Confirmado! Voltando a dormir por 2 horas.")

if __name__ == "__main__":
    executar_monitor()