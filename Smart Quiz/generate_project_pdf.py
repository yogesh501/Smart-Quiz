"""
Smart Quiz - Comprehensive Academic Project Report & Source Code PDF Generator
Generates a complete, publication-grade Computer Science Project Record including:
- Title Header & Table of Contents
- Section 1: Abstract & Objectives
- Section 2: Hardware & Software Requirements (Detailed Tables)
- Section 3: DBMS Architecture & Entity-Relationship Design
- Section 4: Database Schema DDL (schema.sql)
- Section 5: Python Backend Source Code (app.py, database.py, test_app.py, sample seeder)
- Section 6: Frontend Controller & UI Code (quiz.js, main.js, quiz.html, result.html)
- Section 7: Conclusion & Future Scope
"""

import os
import textwrap
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    KeepTogether,
    PageBreak,
    Preformatted,
    Image
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and stamp total page numbers."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#64748B"))

        # Running Header (on pages after page 1)
        if self._pageNumber > 1:
            self.drawString(54, letter[1] - 36, "Smart Quiz Web Application — Computer Science Project Report")
            self.drawRightString(letter[0] - 54, letter[1] - 36, "Class 11 Computer Science")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)

        # Running Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(54, 40, letter[0] - 54, 40)

        self.drawString(54, 26, "Department of Computer Science & Informatics")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 26, page_str)
        self.restoreState()


def get_code_flowables(file_path, display_title, subtitle, chunk_size=48, max_chars=82):
    """
    Reads a source code file, formats each line with clean line numbering,
    wraps long lines, and splits into manageable page-safe Preformatted tables.
    """
    flowables = []

    # Styles
    banner_title_style = ParagraphStyle(
        'BannerTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.white
    )
    banner_sub_style = ParagraphStyle(
        'BannerSub',
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#BFDBFE")
    )
    code_text_style = ParagraphStyle(
        'CodeTextStyle',
        fontName='Courier',
        fontSize=6.8,
        leading=8.6,
        textColor=colors.HexColor("#0F172A")
    )

    # Banner header
    banner_data = [[
        Paragraph(display_title, banner_title_style),
        Paragraph(subtitle, banner_sub_style)
    ]]
    banner_table = Table(banner_data, colWidths=[280, 224])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#1E3A8A")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    flowables.append(banner_table)

    if not os.path.exists(file_path):
        flowables.append(Paragraph(f"<i>File not found at {file_path}</i>", banner_sub_style))
        return flowables

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        raw_lines = f.readlines()

    numbered_lines = []
    line_no = 1
    for r_line in raw_lines:
        line_clean = r_line.rstrip('\r\n')
        # Handle tab indentation
        line_clean = line_clean.replace('\t', '    ')
        
        # Line wrapping if exceeds max_chars
        if len(line_clean) > max_chars:
            indent = len(line_clean) - len(line_clean.lstrip())
            indent_str = " " * indent
            wrapped = textwrap.wrap(line_clean, width=max_chars, subsequent_indent=indent_str + "  ")
            for sub_idx, sub_l in enumerate(wrapped):
                if sub_idx == 0:
                    numbered_lines.append(f"{line_no:4d} | {sub_l}")
                else:
                    numbered_lines.append(f"     | {sub_l}")
        else:
            numbered_lines.append(f"{line_no:4d} | {line_clean}")
        line_no += 1

    # Chunk into page-safe blocks
    for i in range(0, len(numbered_lines), chunk_size):
        chunk = numbered_lines[i:i + chunk_size]
        chunk_text = "\n".join(chunk)
        pre = Preformatted(chunk_text, code_text_style)

        table_data = [[pre]]
        chunk_table = Table(table_data, colWidths=[504])
        chunk_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        flowables.append(chunk_table)
        flowables.append(Spacer(1, 4))

    flowables.append(Spacer(1, 8))
    return flowables


def build_pdf(filename="Smart_Quiz_Project_Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Theme Palette
    primary_color = colors.HexColor("#1E3A8A")   # Navy 900
    secondary_color = colors.HexColor("#2563EB") # Blue 600
    text_color = colors.HexColor("#1F2937")      # Slate 800
    subtext_color = colors.HexColor("#4B5563")   # Slate 600

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=primary_color,
        alignment=1,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=subtext_color,
        alignment=1,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=secondary_color,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13.5,
        textColor=text_color,
        alignment=4,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=13,
        textColor=text_color,
        leftIndent=14,
        spaceAfter=3
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.8,
        textColor=text_color
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=10.8,
        textColor=primary_color
    )

    story = []

    # ==========================================
    # COVER / TITLE BLOCK
    # ==========================================
    story.append(Paragraph("SMART QUIZ WEB APPLICATION", title_style))
    story.append(Paragraph("A Complete Computer Science Project Report & Source Code Listing", subtitle_style))
    story.append(Paragraph("<b>Curriculum:</b> Class 11 Computer Science &nbsp;|&nbsp; <b>Academic Year:</b> 2026-2027 &nbsp;|&nbsp; <b>Tech Stack:</b> Python, Flask, MySQL, SQLite, HTML5, CSS3, JavaScript", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=10))

    # ==========================================
    # SECTION 1: ABSTRACT
    # ==========================================
    story.append(Paragraph("1. ABSTRACT", h1_style))
    story.append(Paragraph(
        "The <b>Smart Quiz Web Application</b> is an interactive, multi-category educational platform engineered to "
        "assess students' conceptual and practical mastery across high school computer science disciplines and general science. "
        "Built strictly following Class 11 CBSE and state curriculum specifications, the project integrates a robust Python Flask backend "
        "with normalized relational database management systems (supporting both <b>MySQL</b> and <b>SQLite</b>), "
        "delivered through an intuitive, student-friendly web interface.",
        body_style
    ))
    story.append(Paragraph(
        "A foundational design principle of the application is <b>tamper-proof evaluation integrity</b>. Traditional client-only quiz "
        "scripts expose correct answers and explanations directly within client HTML/JS, allowing students to inspect solutions using browser "
        "developer tools. In Smart Quiz, all scoring and answer validations are executed strictly <b>server-side</b>. "
        "Correct options, score percentages, and educational explanations are dispatched to the client only after formal submission.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Core Architectural Features:</b>",
        body_style
    ))
    story.append(Paragraph("• <b>Dual Database Engine:</b> Auto-connects to standard MySQL databases with a zero-configuration fallback to an embedded SQLite database (`smart_quiz.db`) for dependable evaluation in any environment.", bullet_style))
    story.append(Paragraph("• <b>Randomized 10-Question Tests:</b> Each test randomly selects 10 questions from a bank of 132+ questions across six subjects: <i>Java, Python, MySQL, DBMS, History, and Science</i>.", bullet_style))
    story.append(Paragraph("• <b>Balanced Option Distribution:</b> Shuffled question options guarantee an equitable ~25% distribution across keys A, B, C, and D, preventing predictable answering patterns.", bullet_style))
    story.append(Paragraph("• <b>Relational Leaderboard & History:</b> Tracks student test history, scores, and completion timestamps in database tables with live real-time search filtering.", bullet_style))
    story.append(Paragraph("• <b>Cross-Platform Responsiveness:</b> Fully responsive design featuring a mobile hamburger drawer, touch targets (&ge; 48px), and public accessibility over local Wi-Fi and cloud.", bullet_style))

    story.append(Spacer(1, 8))

    # ==========================================
    # SECTION 2: HARDWARE & SOFTWARE REQUIREMENTS
    # ==========================================
    story.append(Paragraph("2. HARDWARE AND SOFTWARE REQUIREMENTS", h1_style))
    story.append(Paragraph(
        "The application is engineered with high lightweight efficiency, enabling execution across standard school laboratory computers, cloud servers, and mobile touchscreen devices.",
        body_style
    ))

    story.append(Paragraph("2.1 Hardware Requirements", h2_style))
    hw_data = [
        [
            Paragraph("Component", table_header_style),
            Paragraph("Minimum Specification", table_header_style),
            Paragraph("Recommended Specification", table_header_style),
            Paragraph("Purpose & Role in Project", table_header_style)
        ],
        [
            Paragraph("Processor (CPU)", table_cell_bold),
            Paragraph("Intel Core i3 (2nd Gen) / AMD Ryzen 3 (1.5 GHz)", table_cell_style),
            Paragraph("Intel Core i5 / AMD Ryzen 5 or higher (2.4+ GHz)", table_cell_style),
            Paragraph("Executes Python Flask server, SQL query resolution, and concurrent client requests.", table_cell_style)
        ],
        [
            Paragraph("Memory (RAM)", table_cell_bold),
            Paragraph("2 GB DDR3", table_cell_style),
            Paragraph("4 GB - 8 GB DDR4", table_cell_style),
            Paragraph("Accommodates OS, Python runtime, database caching, and in-memory session pools.", table_cell_style)
        ],
        [
            Paragraph("Storage (Disk)", table_cell_bold),
            Paragraph("200 MB free space", table_cell_style),
            Paragraph("500 MB SSD free space", table_cell_style),
            Paragraph("Stores application code, relational database (`smart_quiz.db`), CSS, JS, and server logs.", table_cell_style)
        ],
        [
            Paragraph("Network Adapter", table_cell_bold),
            Paragraph("Standard Ethernet or Wi-Fi (802.11n)", table_cell_style),
            Paragraph("Gigabit Ethernet / Wi-Fi 5 (802.11ac)", table_cell_style),
            Paragraph("Enables local network binding (0.0.0.0) for multi-device access across lab computers & phones.", table_cell_style)
        ],
        [
            Paragraph("Display / Client", table_cell_bold),
            Paragraph("1024 &times; 768 resolution", table_cell_style),
            Paragraph("1920 &times; 1080 Full HD (PC) or 412 &times; 892 (Android)", table_cell_style),
            Paragraph("Presents responsive user interface across desktop monitors, laptops, and mobile screens.", table_cell_style)
        ]
    ]
    hw_table = Table(hw_data, colWidths=[95, 130, 135, 144])
    hw_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(hw_table)

    story.append(Spacer(1, 6))

    story.append(Paragraph("2.2 Software Requirements", h2_style))
    sw_data = [
        [
            Paragraph("Layer / Category", table_header_style),
            Paragraph("Software / Tool", table_header_style),
            Paragraph("Version / Specification", table_header_style),
            Paragraph("Functionality in Project", table_header_style)
        ],
        [
            Paragraph("Operating System", table_cell_bold),
            Paragraph("Microsoft Windows / Linux / macOS", table_cell_style),
            Paragraph("Windows 10 / 11, Ubuntu 20.04+, macOS 12+", table_cell_style),
            Paragraph("Host environment for server execution and database management.", table_cell_style)
        ],
        [
            Paragraph("Programming Language", table_cell_bold),
            Paragraph("Python", table_cell_style),
            Paragraph("Python 3.10 or 3.11+", table_cell_style),
            Paragraph("Core backend language implementing server routing and scoring algorithms.", table_cell_style)
        ],
        [
            Paragraph("Web Framework", table_cell_bold),
            Paragraph("Flask", table_cell_style),
            Paragraph("Flask 3.1+ (Jinja2 templating engine)", table_cell_style),
            Paragraph("Handles HTTP routes, cookie-signed sessions, and template rendering.", table_cell_style)
        ],
        [
            Paragraph("Database Management", table_cell_bold),
            Paragraph("MySQL Server (with SQLite Fallback)", table_cell_style),
            Paragraph("MySQL 8.0+ / SQLite 3", table_cell_style),
            Paragraph("Relational storage for normalized entities: categories, questions, users, results.", table_cell_style)
        ],
        [
            Paragraph("Database Drivers", table_cell_bold),
            Paragraph("PyMySQL & Python sqlite3", table_cell_style),
            Paragraph("PyMySQL 1.1+ (Python DB-API 2.0)", table_cell_style),
            Paragraph("Facilitates safe, parameterized SQL execution preventing SQL injection.", table_cell_style)
        ],
        [
            Paragraph("Frontend UI & Styling", table_cell_bold),
            Paragraph("HTML5, Vanilla CSS3, JavaScript (ES6+)", table_cell_style),
            Paragraph("Standards-compliant modern web stack", table_cell_style),
            Paragraph("Constructs responsive layouts, modals, validation, and micro-animations.", table_cell_style)
        ],
        [
            Paragraph("Production WSGI", table_cell_bold),
            Paragraph("Waitress & Gunicorn", table_cell_style),
            Paragraph("Waitress 3.0+ / Gunicorn 21.2+", table_cell_style),
            Paragraph("Production-grade WSGI servers supporting concurrent student attempts.", table_cell_style)
        ],
        [
            Paragraph("Client Web Browser", table_cell_bold),
            Paragraph("Modern Web Browser", table_cell_style),
            Paragraph("Google Chrome, Microsoft Edge, Safari, Firefox", table_cell_style),
            Paragraph("Executes frontend UI on desktop computers, Chromebooks, and Android mobile devices.", table_cell_style)
        ]
    ]
    sw_table = Table(sw_data, colWidths=[90, 115, 125, 174])
    sw_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(sw_table)

    story.append(Spacer(1, 10))

    # ==========================================
    # SECTION 3: SYSTEM ARCHITECTURE & DBMS DESIGN
    # ==========================================
    story.append(Paragraph("3. SYSTEM ARCHITECTURE & DBMS DESIGN", h1_style))
    story.append(Paragraph(
        "The database architecture strictly adheres to <b>Third Normal Form (3NF)</b> principles studied in Class 11. "
        "The relational schema divides system state into four logical relations:",
        body_style
    ))
    story.append(Paragraph("1. <b><code>categories</code>:</b> Stores subject categories (Java, Python, MySQL, DBMS, History, Science) with unique codes and UI icons.", bullet_style))
    story.append(Paragraph("2. <b><code>questions</code>:</b> Stores multiple-choice question records, options A&ndash;D, correct keys, and explanations, linked to <code>categories</code> via a Foreign Key with <code>ON DELETE CASCADE</code>.", bullet_style))
    story.append(Paragraph("3. <b><code>users</code>:</b> Stores student session identifiers and names without requiring sensitive personal data or passwords.", bullet_style))
    story.append(Paragraph("4. <b><code>quiz_results</code>:</b> Records completed quiz outcomes, scores, percentages, and timestamps, referencing both <code>users</code> and <code>categories</code>.", bullet_style))
    story.append(Paragraph(
        "To guarantee high query throughput during concurrent tests, indexed lookup structures are defined on <code>category_id</code>, <code>user_id</code>, and <code>completion_date</code>.",
        body_style
    ))

    story.append(PageBreak())

    # ==========================================
    # SECTION 4: SOURCE CODE - DATABASE SCHEMA (schema.sql)
    # ==========================================
    story.append(Paragraph("4. DATABASE DDL SCHEMA CODE", h1_style))
    story.append(Paragraph(
        "The following SQL script (<code>schema.sql</code>) creates the relational database, table structures, "
        "referential constraints, and performance indexes for MySQL and SQLite:",
        body_style
    ))
    story.extend(get_code_flowables("schema.sql", "File: schema.sql", "SQL Data Definition Language (DDL)"))

    story.append(PageBreak())

    # ==========================================
    # SECTION 5: SOURCE CODE - PYTHON BACKEND
    # ==========================================
    story.append(Paragraph("5. BACKEND SOURCE CODE (PYTHON & FLASK)", h1_style))
    story.append(Paragraph(
        "The backend layer comprises the main Flask application controller (<code>app.py</code>), "
        "the database abstraction manager (<code>database.py</code>), the automated test suite (<code>test_app.py</code>), "
        "and the production WSGI runner (<code>run_production.py</code>).",
        body_style
    ))

    # 5.1 app.py
    story.append(Paragraph("5.1 Flask Application Controller (app.py)", h2_style))
    story.append(Paragraph(
        "Implements route management, session state tracking, JSON APIs, and secure server-side score calculation:",
        body_style
    ))
    story.extend(get_code_flowables("app.py", "File: app.py", "Flask Application & Routes"))

    story.append(PageBreak())

    # 5.2 database.py
    story.append(Paragraph("5.2 Database Operations & Fallback Manager (database.py)", h2_style))
    story.append(Paragraph(
        "Manages MySQL connections with automatic fallback to SQLite, parameterized queries, and seeding:",
        body_style
    ))
    story.extend(get_code_flowables("database.py", "File: database.py", "Database Operations Module"))

    story.append(PageBreak())

    # 5.3 test_app.py
    story.append(Paragraph("5.3 Automated Verification Test Suite (test_app.py)", h2_style))
    story.append(Paragraph(
        "Executes 6 automated test cases validating routes, database initialization, session handling, quiz security, and scoring:",
        body_style
    ))
    story.extend(get_code_flowables("test_app.py", "File: test_app.py", "Automated Unit Tests"))

    # 5.4 run_production.py
    story.append(Paragraph("5.4 Production WSGI Server Launcher (run_production.py)", h2_style))
    story.append(Paragraph(
        "Executes high-concurrency production serving via Waitress WSGI on Windows for lab computers and phones:",
        body_style
    ))
    story.extend(get_code_flowables("run_production.py", "File: run_production.py", "Waitress Production WSGI Server"))

    story.append(PageBreak())

    # ==========================================
    # SECTION 6: SOURCE CODE - FRONTEND LOGIC & TEMPLATES
    # ==========================================
    story.append(Paragraph("6. FRONTEND CONTROLLER & UI CODE", h1_style))
    story.append(Paragraph(
        "The client side utilizes Vanilla JavaScript for slide transitions, client-side validation, and modal control, "
        "along with Jinja2 HTML5 semantic templates.",
        body_style
    ))

    # 6.1 quiz.js
    story.append(Paragraph("6.1 Interactive Quiz Engine (static/js/quiz.js)", h2_style))
    story.append(Paragraph(
        "Handles question navigation, single option selection, progress bar updates, palette bubble states, and pre-submit modal:",
        body_style
    ))
    story.extend(get_code_flowables("static/js/quiz.js", "File: static/js/quiz.js", "Quiz State Machine & Controller"))

    story.append(PageBreak())

    # 6.2 main.js
    story.append(Paragraph("6.2 Navigation & Modal Controller (static/js/main.js)", h2_style))
    story.append(Paragraph(
        "Manages mobile hamburger navigation, category selection cards, student registration modal, and leaderboard search:",
        body_style
    ))
    story.extend(get_code_flowables("static/js/main.js", "File: static/js/main.js", "Home & Navigation Controller"))

    story.append(PageBreak())

    # 6.3 templates/quiz.html
    story.append(Paragraph("6.3 Quiz Interface Template (templates/quiz.html)", h2_style))
    story.append(Paragraph(
        "Semantic HTML5 template rendering dynamic questions, 4-option cards, question palette, and confirmation modal:",
        body_style
    ))
    story.extend(get_code_flowables("templates/quiz.html", "File: templates/quiz.html", "Jinja2 Quiz Interface Template"))

    story.append(PageBreak())

    # 6.4 templates/result.html
    story.append(Paragraph("6.4 Results & Explanations Template (templates/result.html)", h2_style))
    story.append(Paragraph(
        "Displays animated score card, performance badges, answer review, and in-depth educational explanations:",
        body_style
    ))
    story.extend(get_code_flowables("templates/result.html", "File: templates/result.html", "Jinja2 Results & Review Template"))

    story.append(PageBreak())

    # ==========================================
    # SECTION 7: APPLICATION SCREENSHOTS (PC & ANDROID)
    # ==========================================
    story.append(Paragraph("7. APPLICATION SCREENSHOTS (DESKTOP & ANDROID VIEWS)", h1_style))
    story.append(Paragraph(
        "The following figures illustrate the visual interface and layout responsiveness across both desktop personal computers "
        "(1280 &times; 820 resolution) and Android mobile devices (412 &times; 892 viewport):",
        body_style
    ))

    screenshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

    shot_pairs = [
        (
            "7.1 Home Page & Category Selection",
            "Displays application title, welcome message, live database engine badge, stats summary cards, and 6 subject category cards.",
            "pc_home.png",
            "android_home.png"
        ),
        (
            "7.2 Interactive 10-Question Quiz Interface",
            "Demonstrates dynamic question counter, animated progress bar, question palette bubbles (1–10), and single-choice answer option cards.",
            "pc_quiz.png",
            "android_quiz.png"
        ),
        (
            "7.3 Results & Score Evaluation Page",
            "Highlights circular score indicator, performance-based motivational badge, score breakdown grid, and answer review with educational explanations.",
            "pc_result.png",
            "android_result.png"
        ),
        (
            "7.4 Leaderboard & Student Submission History",
            "Presents persistent database records of student attempts, percentages, completion timestamps, and instant real-time live search filter.",
            "pc_leaderboard.png",
            "android_leaderboard.png"
        )
    ]

    img_title_pc = ParagraphStyle('ImgTitlePC', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=primary_color, alignment=1)
    img_title_mob = ParagraphStyle('ImgTitleMob', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=secondary_color, alignment=1)

    for sub_title, sub_desc, pc_file, mob_file in shot_pairs:
        pc_path = os.path.join(screenshots_dir, pc_file)
        mob_path = os.path.join(screenshots_dir, mob_file)

        story.append(Paragraph(sub_title, h2_style))
        story.append(Paragraph(sub_desc, body_style))
        story.append(Spacer(1, 4))

        cells = []
        if os.path.exists(pc_path) and os.path.exists(mob_path):
            pc_img = Image(pc_path, width=315, height=202)
            mob_img = Image(mob_path, width=152, height=329)

            col1_content = [Paragraph("<b>Desktop / PC View (1280 &times; 820)</b>", img_title_pc), Spacer(1, 4), pc_img]
            col2_content = [Paragraph("<b>Android Mobile View (412 &times; 892)</b>", img_title_mob), Spacer(1, 4), mob_img]

            grid_table = Table([[col1_content, col2_content]], colWidths=[330, 174])
            grid_table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('LEFTPADDING', (0, 0), (-1, -1), 4),
                ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(grid_table)
        story.append(PageBreak())

    # ==========================================
    # SECTION 8: CONCLUSION & FUTURE SCOPE
    # ==========================================
    story.append(Paragraph("8. CONCLUSION AND FUTURE SCOPE", h1_style))
    story.append(Paragraph(
        "The <b>Smart Quiz Web Application</b> successfully fulfills and exceeds all criteria specified for the "
        "Class 11 Computer Science Project evaluation. By harmonizing Python Flask server programming, relational "
        "database management systems, and modern, responsive frontend web technologies, the project delivers an end-to-end, "
        "production-grade educational evaluation solution.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Summary of Accomplishments:</b>",
        body_style
    ))
    story.append(Paragraph("• <b>Rigorous Curriculum Integration:</b> Demonstrates hands-on proficiency in Python backend programming, relational DBMS normalization, primary/foreign key integrity, MySQL and SQLite querying, and foundational Java OOP principles.", bullet_style))
    story.append(Paragraph("• <b>High Assessment Integrity:</b> Secure server-side grading completely prevents answer inspection tampering in student web browsers.", bullet_style))
    story.append(Paragraph("• <b>Balanced Option Distribution:</b> Shuffled question options guarantee balanced ~25% frequencies across A, B, C, and D.", bullet_style))
    story.append(Paragraph("• <b>Dual-Device Mobile & Desktop Responsiveness:</b> Collapsible mobile hamburger drawer, touch-friendly 48px tap targets, and fluid responsive grid layouts support Android devices and computers identically.", bullet_style))
    story.append(Paragraph("• <b>Multi-Tier Deployment Architecture:</b> Operates smoothly in local development, production multi-threaded Windows WSGI (Waitress), school Wi-Fi networks, and public HTTPS cloud links.", bullet_style))

    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Future Scope & Enhancements:</b>", h2_style))
    story.append(Paragraph(
        "While the current release provides an all-inclusive testing platform, the modular architecture facilitates seamless future enhancements:<br/>"
        "1. <b>Timed Test Sessions:</b> Inclusion of a real-time countdown timer with automated submission upon expiration.<br/>"
        "2. <b>Teacher Administration Portal:</b> An authenticated portal allowing instructors to add, edit, or categorize custom questions directly from the web browser.<br/>"
        "3. <b>Student Account Profiles:</b> Optional login profiles providing graphical tracking of a student's score progression over time.<br/>"
        "4. <b>Automated PDF Report Card Generation:</b> Exporting personalized, downloadable student performance certificates upon test completion.",
        body_style
    ))

    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=8))
    story.append(Paragraph(
        "<i>Report prepared and verified for Class 11 Computer Science Practical Project Submission.</i>",
        meta_style
    ))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[PDF] Successfully created: {os.path.abspath(filename)}")


if __name__ == "__main__":
    build_pdf()
