import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_homenagem():
    mensagens = [
        "Eterno Ganley",
        "Obrigado por tudo",
        "Você sempre será nosso futuro Olympia 🏅"
    ]
    
    for msg in mensagens:
        limpar_tela()
        painel = Panel(
            f"[white]{msg}[/white]", 
            title="EM MEMÓRIA DE GABRIEL GANLEY", 
            title_align="left",
            expand=False
        )
        console.print(painel)
        time.sleep(3.0)

def exibir_musica():
    limpar_tela()
    console.print("[bold white]JANE![/bold white]\n")
    time.sleep(2.0)
    
    # Cada tupla contém: (Texto formatado com cores do Rich, tempo de espera antes da próxima linha)
    # Cores usadas: [blue] para amarelo, [grey50] para o efeito de fade/cinza do Spotify
    letra = [
        # --- ESTROFE 1 (A do vídeo) ---
        ("you're early", 1.8),
        ("[blue]your life's work is dirtied by the fools[/blue]", 2.8),
        ("who adore you", 1.8),
        ("only to find", 1.4),
        ("[blue]only to find you out[/blue]", 3.2),
        ("", 0.5),
        ("they saw you", 1.8),
        ("dressing in the backroom now they'll pay!", 3.2),
        ("[grey50]what they owe you[/grey50]", 4.5),
        ("", 1.0),
        
        # --- REFRÃO ---
        ("[blue]oh jane,[/blue]", 2.0),
        ("is it sub-text or a sign?", 3.5),
        ("[blue]oh jane,[/blue]", 2.0),
        ("are we running out of time?", 4.0),
        ("", 0.5),
        
        # --- ESTROFE 2 ---
        ("you're clever", 2.2),
        ("[blue]you build a wall of paper just to see[/blue]", 2.8),
        ("who could climb it", 1.8),
        ("only to find", 1.4),
        ("[blue]only to find it falls[/blue]", 3.5),
        ("", 0.5),
        ("they saw you", 1.8),
        ("tearing down the rafters now they'll pay!", 3.2),
        ("[grey50]what they owe you[/grey50]", 4.5),
        ("", 1.0),
        
        # --- REFRÃO FINAL ---
        ("[blue]oh jane,[/blue]", 2.0),
        ("is it sub-text or a sign?", 3.5),
        ("[blue]oh jane,[/blue]", 2.0),
        ("are we running out of time?", 4.5),
        ("", 0.5),
        ("[bold white]running out of time...[/bold white]", 3.0)
    ]
    
    for linha, delay in letra:
        console.print(linha)
        time.sleep(delay)

if __name__ == "__main__":
    exibir_homenagem()
    exibir_musica()