# Digital Clock - README

## 🌍 World Digital Clock Application

A comprehensive multi-timezone clock application with both GUI and console interfaces.

### 📋 Features

#### GUI Version (digital_clock.py)
- 🖥️ Beautiful Tkinter GUI interface
- 📍 12 major world timezones
- ⏰ Real-time updates every second
- 📅 Date display for each timezone
- 🎨 Dark theme with green terminal style
- 🔄 Smooth scrolling interface
- 📊 Automatic layout adjustment

#### Console Version (console_clock.py)
- 💻 Two modes: Simple and Advanced
- 🎯 Simple Mode: Live updating all timezones
- 📱 Interactive Menu Mode with features:
  - View all timezones
  - View specific timezone details
  - Compare two timezones
  - Time difference calculator
  - Continuous live clock

### 🌐 Included Timezones

1. 🗽 **New York** (America/New_York)
2. 🇬🇧 **London** (Europe/London)
3. 🇫🇷 **Paris** (Europe/Paris)
4. 🇯🇵 **Tokyo** (Asia/Tokyo)
5. 🇦🇺 **Sydney** (Australia/Sydney)
6. 🇦🇪 **Dubai** (Asia/Dubai)
7. 🇮🇳 **Mumbai** (Asia/Kolkata)
8. 🇺🇸 **Los Angeles** (America/Los_Angeles)
9. 🇲🇽 **México** (America/Mexico_City)
10. 🇧🇷 **São Paulo** (America/Sao_Paulo)
11. 🇪🇸 **Madrid** (Europe/Madrid)
12. 🇿🇦 **Johannesburg** (Africa/Johannesburg)

### 🚀 Usage

#### GUI Version

```bash
python digital_clock.py
```

- Displays all timezones in a scrollable window
- Real-time updates every second
- Close window to exit

#### Console Version

```bash
python console_clock.py
```

Then select:
- Option 1: Simple live clock (auto-updating)
- Option 2: Advanced interactive menu

### 📦 Requirements

```
pytz
tkinter (usually included with Python)
```

### 🔧 Installation

```bash
# Install required packages
pip install pytz

# For GUI version, tkinter usually comes with Python
# If not, install: pip install tk
```

### 💡 Examples

#### View All Timezones
```
Select option 1 from the menu
```

#### Compare Two Cities
```
Select option 3
Choose two cities to compare
View time difference
```

#### Calculate Future Time
```
Select option 4
Choose source and destination timezones
Enter hours to add
See what time it will be in another timezone
```

### 🎨 Customization

You can easily customize the application:

1. **Add more timezones**: Edit the `TIMEZONES` list in the script
2. **Change colors**: Modify `bg_color`, `fg_color`, `secondary_bg`, `secondary_fg`
3. **Change fonts**: Update font configurations in `create_ui()`
4. **Modify update frequency**: Change the `time.sleep()` value

### ⚡ Performance

- Lightweight and fast
- Updates every second
- Efficient thread management
- Minimal CPU usage

### 🐛 Troubleshooting

**Problem**: Timezone not found
- **Solution**: Make sure pytz is installed: `pip install pytz`

**Problem**: GUI window not appearing
- **Solution**: Ensure tkinter is installed. For Linux: `sudo apt-get install python3-tk`

**Problem**: Time zones showing wrong time
- **Solution**: Make sure your system clock is synchronized

### 📝 License

MIT License - Feel free to modify and distribute

### 👨‍💻 Author

Created by: Segundo Casado
GitHub: @segundocasado42-png

---

**Enjoy your World Digital Clock!** 🌍⏰
