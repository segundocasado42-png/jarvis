#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JARVIS - AI Personal Assistant
A Python-based AI assistant with voice recognition, web search, and system control
"""

import sys
import logging
from brain import JarvisBrain
from voice_engine import VoiceEngine
from config import JARVIS_NAME, JARVIS_VERSION

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/jarvis.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class JarvisAssistant:
    """Main Jarvis Assistant class"""
    
    def __init__(self):
        logger.info(f"Initializing {JARVIS_NAME} v{JARVIS_VERSION}")
        self.brain = JarvisBrain()
        self.voice = VoiceEngine()
        self.running = False
    
    def greet(self):
        """Greet the user on startup"""
        greeting = f"Hola, soy {JARVIS_NAME}, tu asistente personal. ¿En qué puedo ayudarte?"
        print(f"\n{'='*50}")
        print(f"  {JARVIS_NAME} v{JARVIS_VERSION}")
        print(f"{'='*50}\n")
        print(f"🎤 {greeting}\n")
        self.voice.speak(greeting)
    
    def show_menu(self):
        """Display main menu"""
        menu = """
╔════════════════════════════════════════╗
║         MENÚ PRINCIPAL DE JARVIS       ║
╠════════════════════════════════════════╣
║ 1. Modo voz (escuchar comandos)        ║
║ 2. Modo texto (escribir comandos)      ║
║ 3. Mostrar comandos disponibles        ║
║ 4. Configuración                       ║
║ 5. Salir                               ║
╚════════════════════════════════════════╝
"""
        print(menu)
    
    def show_commands(self):
        """Display available commands"""
        commands = """
╔════════════════════════════════════════╗
║      COMANDOS DISPONIBLES              ║
╠════════════════════════════════════════╣
║ • Hola / Saludar                       ║
║ • ¿Qué hora es?                        ║
║ • ¿Qué fecha es?                       ║
║ • Busca [término]                      ║
║ • Wikipedia [término]                  ║
║ • Clima en [ciudad]                    ║
║ • Noticias                             ║
║ • Abrir [aplicación]                   ║
║ • Cerrar [aplicación]                  ║
║ • Información del sistema              ║
║ • Nota [contenido]                     ║
║ • Leer notas                           ║
║ • Youtube [video]                      ║
║ • Música [canción]                     ║
║ • Apagar                               ║
║ • Reiniciar                            ║
╚════════════════════════════════════════╝
"""
        print(commands)
    
    def voice_mode(self):
        """Voice mode - listen and process commands"""
        print("\n🎤 Modo voz activado. Di tus comandos (di 'salir' para volver)...\n")
        self.voice.speak("Estoy escuchando. ¿Qué necesitas?")
        
        while self.running:
            try:
                user_input = self.voice.listen(timeout=10)
                
                if user_input:
                    if "salir" in user_input.lower():
                        self.voice.speak("Volviendo al menú principal")
                        break
                    
                    print(f"👤 Usuario: {user_input}")
                    self.brain.process_command(user_input)
                else:
                    self.voice.speak("No entendí lo que dijiste. Intenta de nuevo")
            
            except KeyboardInterrupt:
                print("\n⏹️  Modo voz detenido")
                break
            except Exception as e:
                logger.error(f"Error in voice mode: {e}")
                self.voice.speak("Ocurrió un error. Intenta de nuevo")
    
    def text_mode(self):
        """Text mode - type commands"""
        print("\n⌨️  Modo texto activado. Escribe tus comandos (escribe 'salir' para volver)...\n")
        
        while self.running:
            try:
                user_input = input("📝 Tú: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == "salir":
                    print("Volviendo al menú principal\n")
                    break
                
                self.brain.process_command(user_input)
            
            except KeyboardInterrupt:
                print("\n⏹️  Modo texto detenido")
                break
            except Exception as e:
                logger.error(f"Error in text mode: {e}")
                print(f"❌ Error: {e}")
    
    def settings(self):
        """Settings menu"""
        settings_menu = """
╔════════════════════════════════════════╗
║         CONFIGURACIÓN DE JARVIS        ║
╠════════════════════════════════════════╣
║ 1. Velocidad de voz                    ║
║ 2. Volumen                             ║
║ 3. Idioma                              ║
║ 4. Volver                              ║
╚════════════════════════════════════════╝
"""
        print(settings_menu)
        choice = input("Selecciona una opción: ").strip()
        
        if choice == "1":
            print("⚠️  Configuración de velocidad de voz no implementada aún")
        elif choice == "2":
            print("⚠️  Configuración de volumen no implementada aún")
        elif choice == "3":
            print("⚠️  Configuración de idioma no implementada aún")
    
    def run(self):
        """Main loop"""
        self.running = True
        self.greet()
        
        try:
            while self.running:
                self.show_menu()
                choice = input("Selecciona una opción (1-5): ").strip()
                
                if choice == "1":
                    self.voice_mode()
                elif choice == "2":
                    self.text_mode()
                elif choice == "3":
                    self.show_commands()
                elif choice == "4":
                    self.settings()
                elif choice == "5":
                    print("\n👋 ¡Hasta luego! Fue un placer ayudarte.")
                    self.voice.speak("Hasta luego. Fue un placer ayudarte")
                    self.running = False
                else:
                    print("❌ Opción inválida. Intenta de nuevo")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupción del usuario. ¡Hasta luego!")
            self.voice.speak("Hasta luego")
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
            print(f"❌ Error: {e}")
        finally:
            self.running = False


def main():
    """Entry point"""
    try:
        jarvis = JarvisAssistant()
        jarvis.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Error fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
