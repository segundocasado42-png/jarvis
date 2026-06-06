# Jarvis Brain - Natural Language Processing and Command Execution

import logging
import datetime
import webbrowser
import wikipedia
import pywhatkit as kit
from web_search import search_web, get_weather, get_news, get_stock_price
from system_control import open_application, close_application, get_system_info, list_running_processes, lock_screen
from notes_manager import NotesManager
from voice_engine import VoiceEngine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JarvisBrain:
    """Main AI brain of Jarvis"""
    
    def __init__(self):
        self.voice = VoiceEngine()
        self.notes_manager = NotesManager()
        self.commands = self._load_commands()
    
    def _load_commands(self):
        """Load available commands"""
        return {
            "hola": self.greet,
            "buenos días": self.greet,
            "buenas tardes": self.greet,
            "buenas noches": self.greet,
            "ayuda": self.show_help,
            "hora": self.tell_time,
            "fecha": self.tell_date,
            "busca": self.search,
            "google": self.search,
            "wikipedia": self.search_wikipedia,
            "clima": self.get_weather,
            "noticias": self.get_news,
            "abrir": self.open_app,
            "cerrar": self.close_app,
            "información del sistema": self.system_info,
            "cpu": self.system_info,
            "ram": self.system_info,
            "memoria": self.system_info,
            "disco": self.system_info,
            "procesos": self.list_processes,
            "nota": self.add_note,
            "leer notas": self.read_notes,
            "buscar nota": self.search_notes,
            "youtube": self.play_youtube,
            "música": self.play_music,
            "reproducir": self.play_music,
            "apagar": self.shutdown,
            "reiniciar": self.restart,
            "bloquear": self.lock_screen,
            "precio": self.get_stock_price,
            "stock": self.get_stock_price,
            "convertir": self.convert_currency,
        }
    
    def process_command(self, user_input):
        """Process user command and execute appropriate action"""
        if not user_input:
            return
        
        user_input_lower = user_input.lower().strip()
        
        # Check for exact command matches
        for command, function in self.commands.items():
            if command in user_input_lower:
                try:
                    function(user_input)
                    return
                except Exception as e:
                    logger.error(f"Error executing command: {e}")
                    try:
                        self.voice.speak(f"Ocurrió un error: {str(e)}")
                    except:
                        pass
                    return
        
        # If no command matched, try web search
        self.search(user_input)
    
    def greet(self, user_input):
        """Greet the user"""
        greetings = [
            "Hola, soy Jarvis, tu asistente personal.",
            "Saludos, ¿en qué puedo ayudarte?",
            "Estoy aquí para ayudarte con lo que necesites.",
            "¿Qué necesitas hoy?",
        ]
        import random
        response = random.choice(greetings)
        print(f"🤖 {response}")
        try:
            self.voice.speak(response)
        except:
            pass
    
    def show_help(self, user_input):
        """Show help information"""
        help_text = "Puedo ayudarte con búsquedas, clima, noticias, notas, controlar tu PC y mucho más. Prueba con 'mostrar comandos' para ver todas las opciones."
        print(f"ℹ️  {help_text}")
        try:
            self.voice.speak(help_text)
        except:
            pass
    
    def tell_time(self, user_input):
        """Tell current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S")
        response = f"Son las {time_str}"
        print(f"⏰ {response}")
        try:
            self.voice.speak(response)
        except:
            pass
    
    def tell_date(self, user_input):
        """Tell current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%d de %B de %Y")
        response = f"Hoy es {date_str}"
        print(f"📅 {response}")
        try:
            self.voice.speak(response)
        except:
            pass
    
    def search(self, user_input):
        """Search on the web"""
        query = user_input.replace("busca", "").replace("google", "").strip()
        if query:
            print(f"🔍 Buscando: {query}")
            try:
                self.voice.speak(f"Buscando {query}")
            except:
                pass
            results = search_web(query)
            if results:
                for i, result in enumerate(results, 1):
                    print(f"\n{i}. {result.get('title', 'Sin título')}")
                    print(f"   {result.get('snippet', '')[:100]}...")
                print(f"\n✅ He encontrado {len(results)} resultados")
                try:
                    self.voice.speak("He encontrado algunos resultados")
                except:
                    pass
            else:
                print("❌ No encontré resultados")
                try:
                    self.voice.speak("No encontré resultados")
                except:
                    pass
    
    def search_wikipedia(self, user_input):
        """Search on Wikipedia"""
        query = user_input.replace("wikipedia", "").strip()
        if query:
            try:
                print(f"📖 Buscando en Wikipedia: {query}")
                result = wikipedia.summary(query, sentences=3, auto_suggest=True)
                print(f"\n{result}")
                try:
                    self.voice.speak(result)
                except:
                    pass
            except wikipedia.exceptions.DisambiguationError as e:
                print("⚠️  El término es ambiguo")
                try:
                    self.voice.speak("El término es ambiguo. Intenta ser más específico")
                except:
                    pass
            except wikipedia.exceptions.PageError:
                print("❌ No encontré información en Wikipedia")
                try:
                    self.voice.speak("No encontré información en Wikipedia")
                except:
                    pass
    
    def get_weather(self, user_input):
        """Get weather information"""
        city = user_input.replace("clima", "").strip() or "Madrid"
        print(f"🌤️  Obteniendo clima de {city}")
        weather = get_weather(city)
        if weather:
            print(f"\n{weather}")
            try:
                self.voice.speak(weather)
            except:
                pass
        else:
            print("❌ No pude obtener la información del clima")
            try:
                self.voice.speak("No pude obtener la información del clima")
            except:
                pass
    
    def get_news(self, user_input):
        """Get latest news"""
        print("📰 Obteniendo noticias...")
        news = get_news()
        if news:
            print(f"\n{news}")
            try:
                self.voice.speak(news)
            except:
                pass
        else:
            print("❌ No pude obtener las noticias")
            try:
                self.voice.speak("No pude obtener las noticias")
            except:
                pass
    
    def open_app(self, user_input):
        """Open an application"""
        app = user_input.replace("abrir", "").strip()
        if app:
            print(f"📂 Abriendo {app}")
            success = open_application(app)
            if success:
                print(f"✅ {app} abierto")
                try:
                    self.voice.speak(f"Abriendo {app}")
                except:
                    pass
            else:
                print(f"❌ No pude abrir {app}")
                try:
                    self.voice.speak(f"No pude abrir {app}")
                except:
                    pass
    
    def close_app(self, user_input):
        """Close an application"""
        app = user_input.replace("cerrar", "").strip()
        if app:
            print(f"❌ Cerrando {app}")
            success = close_application(app)
            if success:
                print(f"✅ {app} cerrado")
                try:
                    self.voice.speak(f"Cerrando {app}")
                except:
                    pass
            else:
                print(f"❌ No pude cerrar {app}")
                try:
                    self.voice.speak(f"No pude cerrar {app}")
                except:
                    pass
    
    def system_info(self, user_input):
        """Get system information"""
        print("💻 Obteniendo información del sistema")
        info = get_system_info()
        if info:
            print(info)
            try:
                self.voice.speak("Aquí está la información de tu sistema")
            except:
                pass
    
    def list_processes(self, user_input):
        """List running processes"""
        print("📊 Procesos activos:")
        processes = list_running_processes()
        if processes:
            for proc in processes:
                print(f"  • {proc['name']}: CPU {proc['cpu']}% | RAM {proc['memory']:.1f}%")
        else:
            print("❌ No se pudieron obtener los procesos")
    
    def add_note(self, user_input):
        """Add a note"""
        note = user_input.replace("nota", "").strip()
        if note:
            self.notes_manager.add_note(note)
            print(f"✅ Nota guardada: {note}")
            try:
                self.voice.speak("Nota guardada")
            except:
                pass
    
    def read_notes(self, user_input):
        """Read all notes"""
        notes = self.notes_manager.get_notes()
        if notes:
            print("📝 Tus notas:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note}")
                try:
                    self.voice.speak(note)
                except:
                    pass
        else:
            print("📝 No tienes notas guardadas")
            try:
                self.voice.speak("No tienes notas guardadas")
            except:
                pass
    
    def search_notes(self, user_input):
        """Search notes by keyword"""
        keyword = user_input.replace("buscar nota", "").replace("busca", "").strip()
        if keyword:
            results = self.notes_manager.search_notes(keyword)
            if results:
                print(f"📝 Notas encontradas con '{keyword}':")
                for note in results:
                    print(f"  • {note}")
            else:
                print(f"❌ No encontré notas con '{keyword}'")
    
    def play_youtube(self, user_input):
        """Play video on YouTube"""
        query = user_input.replace("youtube", "").strip()
        if query:
            print(f"🎥 Buscando en YouTube: {query}")
            try:
                self.voice.speak(f"Buscando {query} en YouTube")
            except:
                pass
            try:
                kit.playonyt(query)
                print(f"✅ Reproduciendo: {query}")
            except Exception as e:
                logger.error(f"Error playing YouTube: {e}")
                print("❌ No pude reproducir el video")
                try:
                    self.voice.speak("No pude reproducir el video")
                except:
                    pass
    
    def play_music(self, user_input):
        """Play music"""
        song = user_input.replace("música", "").replace("reproducir", "").strip()
        if song:
            print(f"🎵 Buscando música: {song}")
            try:
                self.voice.speak(f"Reproduciendo {song}")
            except:
                pass
            try:
                kit.playonyt(song)
                print(f"✅ Reproduciendo: {song}")
            except Exception as e:
                logger.error(f"Error playing music: {e}")
    
    def get_stock_price(self, user_input):
        """Get stock price"""
        symbol = user_input.replace("precio", "").replace("stock", "").strip().upper()
        if symbol:
            print(f"💰 Buscando precio de {symbol}")
            result = get_stock_price(symbol)
            if result:
                print(f"✅ {result}")
                try:
                    self.voice.speak(result)
                except:
                    pass
            else:
                print(f"❌ No encontré información para {symbol}")
    
    def convert_currency(self, user_input):
        """Convert currency"""
        print("💱 Función de conversión de monedas - Próximamente")
    
    def lock_screen(self, user_input):
        """Lock the screen"""
        print("🔒 Bloqueando pantalla...")
        success = lock_screen()
        if success:
            print("✅ Pantalla bloqueada")
            try:
                self.voice.speak("Pantalla bloqueada")
            except:
                pass
    
    def shutdown(self, user_input):
        """Shutdown the computer"""
        print("⚠️  El equipo se apagará en 10 segundos")
        try:
            self.voice.speak("Apagando el equipo en 10 segundos")
        except:
            pass
        import os
        import time
        time.sleep(10)
        os.system("shutdown /s /t 1" if os.name == 'nt' else "shutdown -h now")
    
    def restart(self, user_input):
        """Restart the computer"""
        print("⚠️  El equipo se reiniciará en 10 segundos")
        try:
            self.voice.speak("Reiniciando el equipo en 10 segundos")
        except:
            pass
        import os
        import time
        time.sleep(10)
        os.system("shutdown /r /t 1" if os.name == 'nt' else "shutdown -r now")
