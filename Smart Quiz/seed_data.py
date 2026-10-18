"""
Smart Quiz - Seed Data Module
Populates initial categories and at least 20+ comprehensive questions per category
(Total: 132+ beginner-friendly questions tailored for 11th standard students).
"""

CATEGORIES = [
    {
        "name": "Java Programming",
        "code": "java",
        "description": "Master Java basics including syntax, primitive types, loops, conditionals, and Object-Oriented Programming (OOP) concepts.",
        "icon": "code-slash"
    },
    {
        "name": "Python Programming",
        "code": "python",
        "description": "Test your Python fundamentals: data types, indentation, if-else logic, loops, lists, dictionaries, and user-defined functions.",
        "icon": "terminal"
    },
    {
        "name": "MySQL",
        "code": "mysql",
        "description": "Explore relational queries: SELECT, INSERT, UPDATE, DELETE, filtering with WHERE, sorting with ORDER BY, and Primary Keys.",
        "icon": "server"
    },
    {
        "name": "DBMS",
        "code": "dbms",
        "description": "Understand core Database Management System concepts: tables, tuples, primary/foreign keys, 1NF-3NF normalization, and ACID properties.",
        "icon": "database"
    },
    {
        "name": "History",
        "code": "history",
        "description": "Travel through time: Indus Valley civilization, Maurya dynasty, Indian freedom movement, national leaders, and world milestones.",
        "icon": "landmark"
    },
    {
        "name": "Science",
        "code": "science",
        "description": "Discover the wonders of Physics laws, chemical reactions, cell biology, solar system astronomy, and historic scientific breakthroughs.",
        "icon": "atom"
    }
]

# 22 Questions for each category (Total: 132 questions)

# 22 Balanced & Shuffled Questions for each category (Total: 132 questions)
QUESTIONS = {   'dbms': [   {   'correct_option': 'B',
                    'explanation': 'DBMS stands for Database Management System, software designed to store, retrieve, '
                                   'define, and manage structured data.',
                    'option_a': 'Direct Base Memory Storage',
                    'option_b': 'Database Management System',
                    'option_c': 'Data Building Main System',
                    'option_d': 'Data Backup Management Service',
                    'question_text': 'What does DBMS stand for?'},
                {   'correct_option': 'C',
                    'explanation': "In relational database theory, a row is called a 'Tuple', a column is an "
                                   "'Attribute', and a table is a 'Relation'.",
                    'option_a': 'Domain',
                    'option_b': 'Relation',
                    'option_c': 'Tuple',
                    'option_d': 'Attribute',
                    'question_text': 'In a relational database, what is another formal term for a row in a table?'},
                {   'correct_option': 'D',
                    'explanation': 'An Attribute represents a named property or field describing an entity, '
                                   'corresponding to a table column.',
                    'option_a': 'Record',
                    'option_b': 'Tuple',
                    'option_c': 'Entity',
                    'option_d': 'Attribute',
                    'question_text': 'What is a column in a database table called in relational terminology?'},
                {   'correct_option': 'A',
                    'explanation': 'A DBMS centralizes data, eliminating unnecessary duplication (redundancy) and '
                                   'preventing inconsistencies across files.',
                    'option_a': 'Reduced data redundancy and improved data consistency',
                    'option_b': 'Increased data redundancy',
                    'option_c': 'Higher hardware cost',
                    'option_d': 'Lack of security',
                    'question_text': 'What is a major advantage of using a DBMS over a traditional file-processing '
                                     'system?'},
                {   'correct_option': 'A',
                    'explanation': 'A Foreign Key in a child table points to the Primary Key in a parent table, '
                                   'enforcing referential integrity.',
                    'option_a': 'A column that refers to the Primary Key of another table to establish a relationship',
                    'option_b': 'A key with no unique values',
                    'option_c': 'An encrypted password key',
                    'option_d': 'A key imported from another country',
                    'question_text': 'What is a Foreign Key in a relational database?'},
                {   'correct_option': 'A',
                    'explanation': 'ACID stands for Atomicity, Consistency, Isolation, and Durability. Atomicity '
                                   "ensures all operations succeed or all are rolled back ('all-or-nothing').",
                    'option_a': 'Atomicity',
                    'option_b': 'Availability',
                    'option_c': 'Accuracy',
                    'option_d': 'Authentication',
                    'question_text': "What does the 'A' in the ACID properties of a database transaction stand for?"},
                {   'correct_option': 'C',
                    'explanation': 'Normalization organizes tables to reduce redundant data and prevent insertion, '
                                   'deletion, and update anomalies.',
                    'option_a': 'To combine all data into one giant table',
                    'option_b': 'To delete old records automatically',
                    'option_c': 'To minimize data redundancy and prevent update anomalies',
                    'option_d': 'To make queries run slower',
                    'question_text': 'What is the primary objective of Database Normalization?'},
                {   'correct_option': 'D',
                    'explanation': '1NF requires that each column contains atomic (single-valued) data and each record '
                                   'is unique.',
                    'option_a': 'It is sorted alphabetically',
                    'option_b': 'It has no foreign keys',
                    'option_c': 'It has at least five columns',
                    'option_d': 'Every attribute contains only atomic (indivisible) values and no repeating groups',
                    'question_text': 'A table is in First Normal Form (1NF) if and only if:'},
                {   'correct_option': 'B',
                    'explanation': '2NF requires 1NF compliance and that every non-key attribute is fully functionally '
                                   'dependent on the primary key (no partial dependencies).',
                    'option_a': 'It must have no primary key',
                    'option_b': 'It must be in 1NF and have no partial functional dependency on a composite candidate '
                                'key',
                    'option_c': 'It must be split into at least 10 tables',
                    'option_d': 'It must contain only integers',
                    'question_text': 'What condition must be satisfied for a relation to be in Second Normal Form '
                                     '(2NF)?'},
                {   'correct_option': 'B',
                    'explanation': '3NF removes transitive dependencies (where a non-prime attribute depends on '
                                   'another non-prime attribute).',
                    'option_a': 'Foreign keys',
                    'option_b': 'Transitive dependencies',
                    'option_c': 'Primary keys',
                    'option_d': 'Numeric data',
                    'question_text': 'A table in 2NF is in Third Normal Form (3NF) if it has no:'},
                {   'correct_option': 'C',
                    'explanation': 'A Composite Key is a primary key that combines two or more columns to form a '
                                   'unique identifier.',
                    'option_a': 'Foreign Key',
                    'option_b': 'Secondary Key',
                    'option_c': 'Composite Key',
                    'option_d': 'Super Key',
                    'question_text': 'Which key consists of two or more columns that together uniquely identify a '
                                     'record in a table?'},
                {   'correct_option': 'B',
                    'explanation': 'One classroom contains multiple students, but each student belongs to only one '
                                   'classroom, forming a One-to-Many (1:N) relationship.',
                    'option_a': 'Self-referencing',
                    'option_b': 'One-to-Many (1:N)',
                    'option_c': 'One-to-One (1:1)',
                    'option_d': 'Many-to-Many (M:N)',
                    'question_text': 'What type of relationship exists between a Student and a Classroom if one '
                                     'classroom has many students?'},
                {   'correct_option': 'C',
                    'explanation': 'An Entity-Relationship (ER) diagram models the conceptual structure of a database '
                                   'using entities, attributes, and relationships.',
                    'option_a': 'Flowchart',
                    'option_b': 'Pie Chart',
                    'option_c': 'ER Diagram (Entity-Relationship Diagram)',
                    'option_d': 'Use Case Diagram',
                    'question_text': 'What diagramming tool visually represents database entities, attributes, and '
                                     'their relationships?'},
                {   'correct_option': 'B',
                    'explanation': 'DDL (Data Definition Language) includes commands like CREATE, ALTER, and DROP that '
                                   'define or alter database schema.',
                    'option_a': 'Direct Data Logic',
                    'option_b': 'Data Definition Language',
                    'option_c': 'Dynamic Database Loader',
                    'option_d': 'Data Distribution Link',
                    'question_text': 'What does DDL stand for in database terminology?'},
                {   'correct_option': 'D',
                    'explanation': 'DML (Data Manipulation Language) commands manage and manipulate the actual data '
                                   'inside existing tables.',
                    'option_a': 'DDL (Data Definition Language)',
                    'option_b': 'TCL (Transaction Control Language)',
                    'option_c': 'DCL (Data Control Language)',
                    'option_d': 'DML (Data Manipulation Language)',
                    'question_text': 'Which category of SQL commands includes INSERT, UPDATE, and DELETE?'},
                {   'correct_option': 'A',
                    'explanation': 'Data redundancy occurs when the same piece of information is stored repeatedly in '
                                   'multiple tables or files.',
                    'option_a': 'Unnecessary duplication of identical data across multiple places',
                    'option_b': 'Encrypting confidential data',
                    'option_c': 'Loss of data due to power failure',
                    'option_d': 'High speed query performance',
                    'question_text': "What does 'Data Redundancy' mean in database terminology?"},
                {   'correct_option': 'B',
                    'explanation': 'Referential Integrity ensures that relationships between tables remain consistent '
                                   'and no orphan records exist.',
                    'option_a': 'Entity Integrity Constraint',
                    'option_b': 'Referential Integrity Constraint',
                    'option_c': 'Key Constraint',
                    'option_d': 'Domain Integrity Constraint',
                    'question_text': 'What rule ensures that a foreign key value must either match an existing primary '
                                     'key value or be NULL?'},
                {   'correct_option': 'D',
                    'explanation': 'A DBA is responsible for database installation, configuration, security, user '
                                   'privileges, backup, and performance tuning.',
                    'option_a': 'Designing hardware circuit boards',
                    'option_b': 'Manufacturing computers',
                    'option_c': 'Writing end-user blog articles',
                    'option_d': 'Managing, securing, optimizing, and backing up the database system',
                    'question_text': 'What is the role of a Database Administrator (DBA)?'},
                {   'correct_option': 'A',
                    'explanation': 'The Internal (or Physical) level defines the physical storage structures, paths, '
                                   'and access paths on secondary storage.',
                    'option_a': 'Internal / Physical Level',
                    'option_b': 'Logical Level',
                    'option_c': 'Conceptual Level',
                    'option_d': 'External Level',
                    'question_text': 'What level of the Three-Schema Architecture describes HOW the data is physically '
                                     'stored on disk?'},
                {   'correct_option': 'D',
                    'explanation': 'A Candidate Key is any column or set of columns with unique values that qualifies '
                                   'to be chosen as the Primary Key.',
                    'option_a': 'A column that can only hold numbers',
                    'option_b': 'A key chosen to hold foreign relations',
                    'option_c': 'A key that is always empty',
                    'option_d': 'Any minimal super key capable of uniquely identifying a record',
                    'question_text': "What is a 'Candidate Key' in DBMS?"},
                {   'correct_option': 'A',
                    'explanation': 'Isolation guarantees that concurrently executing transactions do not interfere '
                                   'with each other.',
                    'option_a': 'Isolation',
                    'option_b': 'Independence',
                    'option_c': 'Index',
                    'option_d': 'Integrity',
                    'question_text': "What does the 'I' in ACID stand for?"},
                {   'correct_option': 'C',
                    'explanation': 'A View is a virtual table containing rows and columns defined by an underlying SQL '
                                   'query, without storing its own duplicate data on disk.',
                    'option_a': 'An external programming language',
                    'option_b': 'A physical hardware monitor',
                    'option_c': 'A virtual table based on the result-set of an SQL query',
                    'option_d': 'A backup file',
                    'question_text': "What is a 'View' in a relational database?"}],
    'history': [   {   'correct_option': 'A',
                       'explanation': 'The Indus Valley Civilization (Bronze Age) was renowned for its advanced urban '
                                      'planning, brick houses, and drainage systems.',
                       'option_a': 'Indus Valley Civilization',
                       'option_b': 'Mayan Civilization',
                       'option_c': 'Egyptian Civilization',
                       'option_d': 'Mesopotamian Civilization',
                       'question_text': 'Which ancient civilization flourished along the Indus River valley with '
                                        'prominent cities like Harappa and Mohenjo-daro?'},
                   {   'correct_option': 'C',
                       'explanation': 'Emperor Ashoka embraced Buddhism and non-violence (Ahimsa) after witnessing the '
                                      'immense bloodshed in the Kalinga War around 261 BCE.',
                       'option_a': 'Samudragupta',
                       'option_b': 'Harshavardhana',
                       'option_c': 'Ashoka the Great',
                       'option_d': 'Chandragupta Maurya',
                       'question_text': 'Who was the legendary Mauryan Emperor who embraced Buddhism following the '
                                        'devastating Kalinga War?'},
                   {   'correct_option': 'B',
                       'explanation': 'The Revolt of 1857 began on May 10, 1857 in Meerut, marking a widespread '
                                      'rebellion against British East India Company rule.',
                       'option_a': '1942',
                       'option_b': '1857',
                       'option_c': '1847',
                       'option_d': '1905',
                       'question_text': 'In which year did the historic Revolt of 1857, also known as the First War of '
                                        'Indian Independence, begin?'},
                   {   'correct_option': 'A',
                       'explanation': 'Mahatma Gandhi led India to freedom through non-violent civil disobedience and '
                                      "satyagraha, earning the title 'Father of the Nation'.",
                       'option_a': 'Mahatma Gandhi',
                       'option_b': 'Dr. B.R. Ambedkar',
                       'option_c': 'Jawaharlal Nehru',
                       'option_d': 'Subhash Chandra Bose',
                       'question_text': "Who is revered as the 'Father of the Indian Nation'?"},
                   {   'correct_option': 'A',
                       'explanation': 'India achieved independence from British rule at midnight on 15 August 1947.',
                       'option_a': '15 August 1947',
                       'option_b': '26 January 1950',
                       'option_c': '2 October 1869',
                       'option_d': '14 November 1947',
                       'question_text': 'On which historic date did India gain independence from British colonial '
                                        'rule?'},
                   {   'correct_option': 'B',
                       'explanation': 'Dr. Bhimrao Ramji Ambedkar chaired the Drafting Committee and is acknowledged '
                                      'as the chief architect of the Constitution of India.',
                       'option_a': 'Abul Kalam Azad',
                       'option_b': 'Dr. B.R. Ambedkar',
                       'option_c': 'Sardar Vallabhbhai Patel',
                       'option_d': 'Dr. Rajendra Prasad',
                       'question_text': 'Who served as the Chairman of the Drafting Committee of the Indian '
                                        'Constitution?'},
                   {   'correct_option': 'D',
                       'explanation': "The Quit India Movement ('Bharat Chhodo Andolan') was launched at the Bombay "
                                      "session of the All-India Congress Committee in August 1942 with the call 'Do or "
                                      "Die'.",
                       'option_a': 'Swadeshi Movement',
                       'option_b': 'Civil Disobedience Movement',
                       'option_c': 'Non-Cooperation Movement',
                       'option_d': 'Quit India Movement',
                       'question_text': 'Which historic movement was launched by Mahatma Gandhi in August 1942 '
                                        'demanding an immediate end to British rule?'},
                   {   'correct_option': 'C',
                       'explanation': "Pandit Jawaharlal Nehru took oath as independent India's first Prime Minister "
                                      'on August 15, 1947.',
                       'option_a': 'Lal Bahadur Shastri',
                       'option_b': 'Indira Gandhi',
                       'option_c': 'Jawaharlal Nehru',
                       'option_d': 'Morarji Desai',
                       'question_text': 'Who was the first Prime Minister of independent India?'},
                   {   'correct_option': 'B',
                       'explanation': "Sardar Vallabhbhai Patel, India's first Deputy Prime Minister and Home "
                                      'Minister, united the princely states through statesmanship and resolve.',
                       'option_a': 'Bhagat Singh',
                       'option_b': 'Sardar Vallabhbhai Patel',
                       'option_c': 'Lala Lajpat Rai',
                       'option_d': 'Bal Gangadhar Tilak',
                       'question_text': "Who was known as the 'Iron Man of India' for integrating over 500 princely "
                                        'states into the Indian Union?'},
                   {   'correct_option': 'D',
                       'explanation': 'British troops commanded by General Dyer opened fire on unarmed civilians '
                                      'gathered at Jallianwala Bagh in Amritsar, Punjab.',
                       'option_a': 'Meerut, UP',
                       'option_b': 'Delhi',
                       'option_c': 'Lahore, Punjab',
                       'option_d': 'Amritsar, Punjab',
                       'question_text': 'Where did the tragic Jallianwala Bagh massacre take place on April 13, 1919?'},
                   {   'correct_option': 'D',
                       'explanation': 'Babur defeated Ibrahim Lodi at Panipat in 1526, laying the foundation of the '
                                      'Mughal Empire in India.',
                       'option_a': 'Akbar',
                       'option_b': 'Humayun',
                       'option_c': 'Shah Jahan',
                       'option_d': 'Babur',
                       'question_text': 'Who founded the Mughal Empire in India after winning the First Battle of '
                                        'Panipat in 1526?'},
                   {   'correct_option': 'C',
                       'explanation': 'The Salt Satyagraha began on March 12, 1930 from Sabarmati Ashram to Dandi, '
                                      'breaking the British salt monopoly laws.',
                       'option_a': '1942',
                       'option_b': '1919',
                       'option_c': '1930',
                       'option_d': '1920',
                       'question_text': 'In which year did the Dandi March (Salt Satyagraha) led by Mahatma Gandhi '
                                        'take place?'},
                   {   'correct_option': 'C',
                       'explanation': 'Netaji Subhash Chandra Bose rallied the Indian National Army (INA) with this '
                                      "stirring call to fight for motherland's freedom.",
                       'option_a': 'Bhagat Singh',
                       'option_b': 'Chandra Shekhar Azad',
                       'option_c': 'Subhash Chandra Bose',
                       'option_d': 'Sukhdev Thapar',
                       'question_text': "Which famous freedom fighter popularized the patriotic slogan 'Give me blood, "
                                        "and I shall give you freedom!'?"},
                   {   'correct_option': 'D',
                       'explanation': 'The Renaissance began in Italy and spread across Europe, marking a cultural '
                                      'rebirth after the Middle Ages.',
                       'option_a': 'The Industrial Revolution',
                       'option_b': 'The Cold War',
                       'option_c': 'The Middle Ages',
                       'option_d': 'The Renaissance',
                       'question_text': "Which period in European history (14th–17th centuries) marked the 'rebirth' "
                                        'of art, science, and learning?'},
                   {   'correct_option': 'D',
                       'explanation': 'World War II ended in 1945 following the surrender of Germany in May and Japan '
                                      'in August/September 1945.',
                       'option_a': '1918',
                       'option_b': '1950',
                       'option_c': '1939',
                       'option_d': '1945',
                       'question_text': 'In which year did World War II officially end with the surrender of Axis '
                                        'forces?'},
                   {   'correct_option': 'B',
                       'explanation': 'Chanakya (also known as Kautilya or Vishnugupta), prime advisor to Chandragupta '
                                      'Maurya, authored the Arthashastra.',
                       'option_a': 'Banabhatta',
                       'option_b': 'Chanakya (Kautilya)',
                       'option_c': 'Aryabhata',
                       'option_d': 'Kalidasa',
                       'question_text': 'Who was the author of the ancient political and economic treatise '
                                        "'Arthashastra'?"},
                   {   'correct_option': 'C',
                       'explanation': 'Shaheed Bhagat Singh, Sukhdev, and Rajguru were executed in Lahore Central Jail '
                                      'on March 23, 1931.',
                       'option_a': 'Ashfaqulla Khan',
                       'option_b': 'Ram Prasad Bismil',
                       'option_c': 'Bhagat Singh',
                       'option_d': 'Mangal Pandey',
                       'question_text': 'Which revolutionary martyr smiled and embraced the gallows on March 23, 1931 '
                                        'alongside Rajguru and Sukhdev?'},
                   {   'correct_option': 'A',
                       'explanation': 'Akbar reigned from 1556 to 1605, patronized art and literature, and promoted '
                                      'communal harmony among his subjects.',
                       'option_a': 'Akbar the Great',
                       'option_b': 'Jahangir',
                       'option_c': 'Aurangzeb',
                       'option_d': 'Babur',
                       'question_text': 'Which Mughal Emperor is celebrated for his policy of religious tolerance '
                                        "('Sulh-i-Kul') and founding Fatehpur Sikri?"},
                   {   'correct_option': 'A',
                       'explanation': 'India became a Republic on 26 January 1950, celebrated nationwide every year as '
                                      'Republic Day.',
                       'option_a': '26 January 1950',
                       'option_b': '1 January 1950',
                       'option_c': '26 November 1949',
                       'option_d': '15 August 1947',
                       'question_text': 'In which year did the Constitution of India come into full effect, '
                                        'establishing India as a Sovereign Republic?'},
                   {   'correct_option': 'B',
                       'explanation': 'The United Nations (UN) was established in 1945 by 51 founding nations to '
                                      'prevent future global conflicts.',
                       'option_a': 'European Union',
                       'option_b': 'United Nations (UN)',
                       'option_c': 'League of Nations',
                       'option_d': 'World Bank',
                       'question_text': 'Which international organization was founded on October 24, 1945 following '
                                        'World War II to maintain global peace?'},
                   {   'correct_option': 'A',
                       'explanation': 'Rani Lakshmibai of Jhansi is immortalized as an emblem of bravery and '
                                      'resistance against the British Empire.',
                       'option_a': 'Rani Lakshmibai',
                       'option_b': 'Begum Hazrat Mahal',
                       'option_c': 'Rani Durgavati',
                       'option_d': 'Kittur Chennamma',
                       'question_text': 'Who was the heroic Queen of Jhansi who fought valiantly against British '
                                        'forces during the 1857 Rebellion?'},
                   {   'correct_option': 'B',
                       'explanation': 'Napoleon Bonaparte conquered much of continental Europe before being decisively '
                                      'defeated at the Battle of Waterloo in 1815.',
                       'option_a': 'Louis XIV',
                       'option_b': 'Napoleon Bonaparte',
                       'option_c': 'Robespierre',
                       'option_d': 'Charles de Gaulle',
                       'question_text': 'Which famous French military leader crowned himself Emperor in 1804 and '
                                        'dominated European affairs until Waterloo in 1815?'}],
    'java': [   {   'correct_option': 'C',
                    'explanation': 'Java was originally developed by James Gosling and his team at Sun Microsystems in '
                                   '1995, which was later acquired by Oracle Corporation.',
                    'option_a': 'IBM',
                    'option_b': 'Apple',
                    'option_c': 'Sun Microsystems',
                    'option_d': 'Microsoft',
                    'question_text': 'Which company originally developed Java in 1995?'},
                {   'correct_option': 'D',
                    'explanation': "In Java, standard integer 'int' occupies 4 bytes (32 bits), holding signed values "
                                   'from -2^31 to 2^31-1.',
                    'option_a': '1 byte (8 bits)',
                    'option_b': '2 bytes (16 bits)',
                    'option_c': '8 bytes (64 bits)',
                    'option_d': '4 bytes (32 bits)',
                    'question_text': "What is the size of the 'int' primitive data type in Java?"},
                {   'correct_option': 'A',
                    'explanation': "The 'final' keyword prevents a variable's value from being modified once "
                                   'initialized.',
                    'option_a': 'final',
                    'option_b': 'static',
                    'option_c': 'const',
                    'option_d': 'immutable',
                    'question_text': 'Which keyword is used to declare a constant variable in Java whose value cannot '
                                     'be changed?'},
                {   'correct_option': 'A',
                    'explanation': "The JVM looks for 'public static void main(String[] args)' to begin execution of "
                                   'any standalone Java program.',
                    'option_a': 'public static void main(String[] args)',
                    'option_b': 'public int main(String[] args)',
                    'option_c': 'public void main(String[] args)',
                    'option_d': 'static void main(String args)',
                    'question_text': 'What is the correct syntax for the main method entry point in a standard Java '
                                     'application?'},
                {   'correct_option': 'D',
                    'explanation': "The 'do-while' loop tests its condition at the bottom, so the body always executes "
                                   'at least once.',
                    'option_a': 'for-each loop',
                    'option_b': 'while loop',
                    'option_c': 'for loop',
                    'option_d': 'do-while loop',
                    'question_text': 'Which loop in Java is guaranteed to execute its block at least once before '
                                     'testing the condition?'},
                {   'correct_option': 'A',
                    'explanation': 'The JVM (Java Virtual Machine) translates compiled bytecode into machine-specific '
                                   'instructions at runtime.',
                    'option_a': 'JVM (Java Virtual Machine)',
                    'option_b': 'JDK (Java Development Kit)',
                    'option_c': 'JDB (Java Debugger)',
                    'option_d': 'JRE Compiler',
                    'question_text': 'Which component is responsible for executing Java bytecode (.class files) on any '
                                     'platform?'},
                {   'correct_option': 'C',
                    'explanation': "The 'new' operator allocates memory dynamically on the heap for a new object and "
                                   'calls its constructor.',
                    'option_a': 'make',
                    'option_b': 'instanceof',
                    'option_c': 'new',
                    'option_d': 'create',
                    'question_text': 'Which keyword is used to create an instance or object of a class in Java?'},
                {   'correct_option': 'A',
                    'explanation': "The modulus operator '%' computes the integer remainder after division. 10 divided "
                                   'by 3 leaves a remainder of 1.',
                    'option_a': '1',
                    'option_b': '3',
                    'option_c': '0',
                    'option_d': '3.33',
                    'question_text': 'What will be the output of System.out.println(10 % 3); in Java?'},
                {   'correct_option': 'B',
                    'explanation': "Java uses the primitive keyword 'boolean' (all lowercase) for boolean logic values "
                                   '(true / false).',
                    'option_a': 'bool',
                    'option_b': 'boolean',
                    'option_c': 'BooleanBit',
                    'option_d': 'int',
                    'question_text': 'In Java, which data type is used to store true or false values?'},
                {   'correct_option': 'B',
                    'explanation': "The 'break' statement exits the enclosing loop or switch construct immediately.",
                    'option_a': 'continue',
                    'option_b': 'break',
                    'option_c': 'exit',
                    'option_d': 'stop',
                    'question_text': 'Which statement is used to abruptly terminate a loop or switch block in Java?'},
                {   'correct_option': 'B',
                    'explanation': "Default value for primitive boolean instance fields in Java is 'false'.",
                    'option_a': '0',
                    'option_b': 'false',
                    'option_c': 'null',
                    'option_d': 'true',
                    'question_text': 'What is the default value of an uninitialized instance variable of type boolean '
                                     'in Java?'},
                {   'correct_option': 'D',
                    'explanation': 'The four access levels in Java are private, default (package-private), protected, '
                                   "and public. 'external' is not an access modifier in Java.",
                    'option_a': 'private',
                    'option_b': 'protected',
                    'option_c': 'public',
                    'option_d': 'external',
                    'question_text': 'Which of the following is NOT a valid access modifier in Java?'},
                {   'correct_option': 'A',
                    'explanation': "The 'java.lang' package contains fundamental classes like String, Math, System, "
                                   'and Object, and is imported automatically.',
                    'option_a': 'java.lang',
                    'option_b': 'java.util',
                    'option_c': 'java.io',
                    'option_d': 'java.net',
                    'question_text': 'Which Java package is automatically imported into every Java program without an '
                                     'import statement?'},
                {   'correct_option': 'D',
                    'explanation': 'When javac compiles a .java source file, it produces a .class file containing '
                                   'platform-independent bytecode.',
                    'option_a': '.jar',
                    'option_b': '.jvm',
                    'option_c': '.java',
                    'option_d': '.class',
                    'question_text': 'What is the file extension of a compiled Java file containing bytecode?'},
                {   'correct_option': 'B',
                    'explanation': "'&&' is the short-circuit logical AND operator in Java, evaluating to true only if "
                                   'both operands are true.',
                    'option_a': 'AND',
                    'option_b': '&&',
                    'option_c': '||',
                    'option_d': '&',
                    'question_text': 'Which operator is used for logical AND in Java conditional expressions?'},
                {   'correct_option': 'A',
                    'explanation': 'A constructor has the exact same name as its class and no return type. It is '
                                   'invoked when an object is instantiated.',
                    'option_a': 'Constructor',
                    'option_b': 'Initializer',
                    'option_c': 'Destructor',
                    'option_d': 'Modifier',
                    'question_text': 'What is a special method in Java that has the same name as the class and '
                                     'initializes new objects?'},
                {   'correct_option': 'B',
                    'explanation': "In Java, the '+' operator overloaded for String operands performs concatenation, "
                                   'combining them into "SmartQuiz".',
                    'option_a': 'Syntax Error',
                    'option_b': 'String Concatenation',
                    'option_c': 'Type Casting',
                    'option_d': 'String Replacement',
                    'question_text': "What happens when you add two strings using the '+' operator in Java (e.g. "
                                     '"Smart" + "Quiz")?'},
                {   'correct_option': 'C',
                    'explanation': 'Java arrays are zero-indexed, meaning the first element is at index 0 and the last '
                                   'element is at index (length - 1).',
                    'option_a': 'Length of array',
                    'option_b': '-1',
                    'option_c': '0',
                    'option_d': '1',
                    'question_text': 'What is the index of the first element in a Java array?'},
                {   'correct_option': 'D',
                    'explanation': "Java uses the 'extends' keyword to create an inheritance relationship between "
                                   'classes.',
                    'option_a': 'inherits',
                    'option_b': 'implements',
                    'option_c': 'super',
                    'option_d': 'extends',
                    'question_text': 'Which keyword is used by a class to inherit from a parent class in Java?'},
                {   'correct_option': 'B',
                    'explanation': "Math.sqrt() returns a 'double' precision floating point value, so Math.sqrt(64) "
                                   'evaluates to 8.0.',
                    'option_a': '64.0',
                    'option_b': '8.0',
                    'option_c': '4',
                    'option_d': '8',
                    'question_text': 'What is the result of Math.sqrt(64) in Java?'},
                {   'correct_option': 'C',
                    'explanation': "'for (int i = 0; i < 5; i++)' iterates through i = 0, 1, 2, 3, 4 (5 total "
                                   'iterations).',
                    'option_a': 'for (int i = 1; i <= 4; i++)',
                    'option_b': 'loop (int i = 0; i <= 5)',
                    'option_c': 'for (int i = 0; i < 5; i++)',
                    'option_d': 'for (i = 0 to 4)',
                    'question_text': 'Which loop header is the correct standard Java syntax for counting from 0 up to '
                                     '4?'},
                {   'correct_option': 'C',
                    'explanation': "'this' is a reference variable in Java that refers to the current object whose "
                                   'method or constructor is being invoked.',
                    'option_a': 'current',
                    'option_b': 'self',
                    'option_c': 'this',
                    'option_d': 'super',
                    'question_text': 'Which Java keyword is used to refer to the current instance of the class?'}],
    'mysql': [   {   'correct_option': 'A',
                     'explanation': 'SQL stands for Structured Query Language, the standardized programming language '
                                    'for managing relational databases.',
                     'option_a': 'Structured Query Language',
                     'option_b': 'Simple Query Logic',
                     'option_c': 'Structured Question Language',
                     'option_d': 'Standardized Quick Link',
                     'question_text': 'What does SQL stand for?'},
                 {   'correct_option': 'B',
                     'explanation': 'The SELECT statement queries the database and extracts records from one or more '
                                    'tables.',
                     'option_a': 'RETRIEVE',
                     'option_b': 'SELECT',
                     'option_c': 'GET',
                     'option_d': 'FETCH',
                     'question_text': 'Which SQL command is used to fetch or retrieve data from a database table?'},
                 {   'correct_option': 'D',
                     'explanation': 'The WHERE clause filters rows based on a specified condition (e.g. WHERE score >= '
                                    '80).',
                     'option_a': 'ORDER BY',
                     'option_b': 'HAVING',
                     'option_c': 'GROUP BY',
                     'option_d': 'WHERE',
                     'question_text': 'Which clause is used in SQL to filter rows that meet a specific condition?'},
                 {   'correct_option': 'A',
                     'explanation': 'INSERT INTO table_name (columns) VALUES (values) is used to add new records to a '
                                    'table.',
                     'option_a': 'INSERT INTO',
                     'option_b': 'CREATE ROW',
                     'option_c': 'UPDATE TABLE',
                     'option_d': 'ADD RECORD',
                     'question_text': 'Which SQL command is used to insert a new row of data into a table?'},
                 {   'correct_option': 'B',
                     'explanation': 'The UPDATE statement modifies existing records in a table, usually qualified by a '
                                    'WHERE clause.',
                     'option_a': 'MODIFY',
                     'option_b': 'UPDATE',
                     'option_c': 'CHANGE',
                     'option_d': 'ALTER',
                     'question_text': 'Which SQL statement is used to modify existing data in a table?'},
                 {   'correct_option': 'C',
                     'explanation': 'DELETE FROM table_name WHERE condition is used to delete records from a table.',
                     'option_a': 'REMOVE',
                     'option_b': 'DROP',
                     'option_c': 'DELETE FROM',
                     'option_d': 'CLEAR',
                     'question_text': 'Which command removes existing records from a table in SQL?'},
                 {   'correct_option': 'B',
                     'explanation': 'DESC stands for descending order, sorting results from highest to lowest or Z to '
                                    'A.',
                     'option_a': 'Describes the table schema',
                     'option_b': 'Sorts the result set in descending order',
                     'option_c': 'Sorts the result set in ascending order',
                     'option_d': 'Deletes duplicate entries',
                     'question_text': "What does the SQL command 'ORDER BY column_name DESC' do?"},
                 {   'correct_option': 'D',
                     'explanation': 'A PRIMARY KEY constraint uniquely identifies each row in a database table and '
                                    'strictly rejects NULL values.',
                     'option_a': 'DEFAULT',
                     'option_b': 'CHECK',
                     'option_c': 'FOREIGN KEY',
                     'option_d': 'PRIMARY KEY',
                     'question_text': 'Which constraint uniquely identifies each record in a MySQL table and cannot '
                                      'contain NULL values?'},
                 {   'correct_option': 'B',
                     'explanation': 'SELECT DISTINCT column_name eliminates duplicate rows from the query output.',
                     'option_a': 'UNIQUE_ROWS',
                     'option_b': 'DISTINCT',
                     'option_c': 'DIFFERENT',
                     'option_d': 'NO_DUPLICATES',
                     'question_text': 'Which SQL keyword is used to return only unique, distinct values without '
                                      'duplicates?'},
                 {   'correct_option': 'D',
                     'explanation': 'COUNT(*) or COUNT(column) calculates the total number of records matching the '
                                    'query.',
                     'option_a': 'TOTAL()',
                     'option_b': 'NUMBER()',
                     'option_c': 'SUM()',
                     'option_d': 'COUNT()',
                     'question_text': 'Which aggregate function in SQL returns the total number of rows matching a '
                                      'condition?'},
                 {   'correct_option': 'C',
                     'explanation': "In SQL LIKE clauses, '%' matches any sequence of zero or more characters, while "
                                    "'_' matches exactly one character.",
                     'option_a': '_',
                     'option_b': '*',
                     'option_c': '%',
                     'option_d': '?',
                     'question_text': 'Which wildcard character represents zero or more characters in an SQL LIKE '
                                      'pattern?'},
                 {   'correct_option': 'B',
                     'explanation': 'DROP TABLE table_name permanently removes both the table definition and all of '
                                    'its data.',
                     'option_a': 'TRUNCATE STRUCTURE',
                     'option_b': 'DROP TABLE',
                     'option_c': 'REMOVE TABLE',
                     'option_d': 'DELETE TABLE',
                     'question_text': 'Which command is used to completely remove a table and its entire structure '
                                      'from a MySQL database?'},
                 {   'correct_option': 'A',
                     'explanation': 'CREATE DATABASE database_name; creates a new database container in MySQL.',
                     'option_a': 'CREATE DATABASE name;',
                     'option_b': 'INIT DATABASE name;',
                     'option_c': 'NEW DATABASE name;',
                     'option_d': 'MAKE DATABASE name;',
                     'question_text': 'Which SQL command is used to create a new database in MySQL?'},
                 {   'correct_option': 'C',
                     'explanation': 'MySQL uses the LIMIT clause (e.g. LIMIT 10) to constrain the maximum number of '
                                    'rows returned.',
                     'option_a': 'MAX',
                     'option_b': 'TOP',
                     'option_c': 'LIMIT',
                     'option_d': 'ROWNUM',
                     'question_text': 'Which clause is used in MySQL to limit the number of rows returned by a query?'},
                 {   'correct_option': 'A',
                     'explanation': 'MySQL communicates over TCP/IP port 3306 by default.',
                     'option_a': '3306',
                     'option_b': '1521',
                     'option_c': '5432',
                     'option_d': '8080',
                     'question_text': 'What is the default port number used by a standard MySQL server?'},
                 {   'correct_option': 'A',
                     'explanation': 'The UNION operator combines the result sets of two or more SELECT statements and '
                                    'removes duplicate rows.',
                     'option_a': 'UNION',
                     'option_b': 'JOIN',
                     'option_c': 'MERGE',
                     'option_d': 'INTERSECT',
                     'question_text': 'Which keyword is used to combine results from multiple SELECT statements '
                                      'without duplicate rows?'},
                 {   'correct_option': 'B',
                     'explanation': 'In MySQL, AUTO_INCREMENT automatically generates sequential integer values for '
                                    'primary key columns.',
                     'option_a': 'SERIAL_NUM',
                     'option_b': 'AUTO_INCREMENT',
                     'option_c': 'IDENTITY',
                     'option_d': 'SEQUENCE',
                     'question_text': 'What keyword in MySQL automatically increments a numeric primary key for each '
                                      'newly inserted row?'},
                 {   'correct_option': 'C',
                     'explanation': 'AVG(column_name) returns the arithmetic average of numeric values in the column.',
                     'option_a': 'SUM_AVG()',
                     'option_b': 'MEAN()',
                     'option_c': 'AVG()',
                     'option_d': 'MEDIAN()',
                     'question_text': 'Which SQL aggregate function computes the mathematical average of a numeric '
                                      'column?'},
                 {   'correct_option': 'D',
                     'explanation': 'GROUP BY organizes data into summary rows based on matching values in specified '
                                    'columns.',
                     'option_a': 'COLLECT BY',
                     'option_b': 'ORDER BY',
                     'option_c': 'CLUSTER BY',
                     'option_d': 'GROUP BY',
                     'question_text': 'Which clause is used together with aggregate functions to group rows with '
                                      'identical values?'},
                 {   'correct_option': 'A',
                     'explanation': 'In SQL, NULL signifies an absent, unknown, or undefined value; it is distinct '
                                    'from zero or an empty string.',
                     'option_a': 'Unknown or missing data',
                     'option_b': 'Negative infinity',
                     'option_c': 'Empty string ("")',
                     'option_d': 'Zero (0)',
                     'question_text': 'What does a NULL value indicate in SQL?'},
                 {   'correct_option': 'D',
                     'explanation': 'Because NULL cannot be compared with regular comparison operators (=, !=), SQL '
                                    "requires 'IS NULL' or 'IS NOT NULL'.",
                     'option_a': 'WHERE column EQUALS NULL',
                     'option_b': 'WHERE column = NULL',
                     'option_c': 'WHERE column == NULL',
                     'option_d': 'WHERE column IS NULL',
                     'question_text': 'How do you test for a NULL value in an SQL WHERE clause?'},
                 {   'correct_option': 'C',
                     'explanation': 'ALTER TABLE is a DDL (Data Definition Language) command used to add, modify, or '
                                    'drop columns and constraints in an existing table.',
                     'option_a': 'MODIFY STRUCTURE',
                     'option_b': 'CHANGE TABLE',
                     'option_c': 'ALTER TABLE',
                     'option_d': 'UPDATE TABLE',
                     'question_text': 'Which SQL statement is used to add or modify columns in an existing table?'}],
    'python': [   {   'correct_option': 'B',
                      'explanation': 'Python was created by Dutch programmer Guido van Rossum and first released in '
                                     '1991 at CWI in the Netherlands.',
                      'option_a': 'Bjarne Stroustrup',
                      'option_b': 'Guido van Rossum',
                      'option_c': 'Dennis Ritchie',
                      'option_d': 'James Gosling',
                      'question_text': 'Who created the Python programming language and released it in 1991?'},
                  {   'correct_option': 'D',
                      'explanation': 'Python uses consistent indentation (typically 4 spaces) to delimit blocks of '
                                     'code such as loops, conditionals, and functions.',
                      'option_a': 'BEGIN and END tags',
                      'option_b': 'Parentheses ()',
                      'option_c': 'Semicolons ;',
                      'option_d': 'Indentation (whitespace)',
                      'question_text': 'How does Python define code blocks instead of using curly braces {}?'},
                  {   'correct_option': 'C',
                      'explanation': 'The print() function prints the specified message or variables to the standard '
                                     'output device.',
                      'option_a': 'display()',
                      'option_b': 'write()',
                      'option_c': 'print()',
                      'option_d': 'echo()',
                      'question_text': 'Which built-in Python function displays text and data to the console output?'},
                  {   'correct_option': 'D',
                      'explanation': "The input() function always reads user input as a string ('str'). You must "
                                     'convert it using int() or float() if numerical computation is required.',
                      'option_a': 'float',
                      'option_b': 'bool',
                      'option_c': 'int',
                      'option_d': 'str',
                      'question_text': 'What is the data type of the value returned by the standard input() function '
                                       'in Python?'},
                  {   'correct_option': 'B',
                      'explanation': "In Python, the hash '#' symbol begins a single-line comment, which is ignored by "
                                     'the interpreter.',
                      'option_a': '--',
                      'option_b': '#',
                      'option_c': '/*',
                      'option_d': '//',
                      'question_text': 'What character is used to write a single-line comment in Python?'},
                  {   'correct_option': 'A',
                      'explanation': "The '**' operator represents exponentiation in Python. 2 ** 3 calculates 2 "
                                     'raised to power 3, which equals 8.',
                      'option_a': '8',
                      'option_b': '6',
                      'option_c': '9',
                      'option_d': '5',
                      'question_text': 'What is the output of the expression 2 ** 3 in Python?'},
                  {   'correct_option': 'A',
                      'explanation': "The 'def' keyword is used to define functions in Python (e.g. def "
                                     'calculate_score():).',
                      'option_a': 'def',
                      'option_b': 'define',
                      'option_c': 'function',
                      'option_d': 'func',
                      'question_text': 'Which keyword is used to declare a user-defined function in Python?'},
                  {   'correct_option': 'C',
                      'explanation': 'Lists in Python are mutable ordered sequences defined with square brackets: '
                                     'my_list = [1, 2, 3].',
                      'option_a': 'Tuple',
                      'option_b': 'Set',
                      'option_c': 'List',
                      'option_d': 'Dictionary',
                      'question_text': 'Which of the following data structures in Python is ordered, mutable, and '
                                       'written with square brackets?'},
                  {   'correct_option': 'B',
                      'explanation': '"Smart Quiz" contains 5 letters in \'Smart\', 1 space, and 4 letters in '
                                     "'Quiz', totaling 10 characters.",
                      'option_a': '11',
                      'option_b': '10',
                      'option_c': '9',
                      'option_d': '8',
                      'question_text': 'What will len("Smart Quiz") return in Python?'},
                  {   'correct_option': 'A',
                      'explanation': "The '//' operator is floor division (integer division), which rounds down to the "
                                     'nearest integer. 15 // 4 equals 3.',
                      'option_a': '3',
                      'option_b': '3.0',
                      'option_c': '4',
                      'option_d': '3.75',
                      'question_text': 'What is the result of 15 // 4 in Python?'},
                  {   'correct_option': 'A',
                      'explanation': "Python uses 'elif' (short for else if) for chaining multiple conditional "
                                     'branches.',
                      'option_a': 'elif',
                      'option_b': 'else if',
                      'option_c': 'elseif',
                      'option_d': 'case',
                      'question_text': 'Which keyword is used to test secondary conditions in an if statement in '
                                       'Python?'},
                  {   'correct_option': 'A',
                      'explanation': 'The range(start, stop) function generates numbers from start up to, but not '
                                     'including, the stop value. Hence [1, 2, 3, 4].',
                      'option_a': '[1, 2, 3, 4]',
                      'option_b': '[2, 3, 4, 5]',
                      'option_c': '[0, 1, 2, 3, 4]',
                      'option_d': '[1, 2, 3, 4, 5]',
                      'question_text': 'What will list(range(1, 5)) produce in Python?'},
                  {   'correct_option': 'C',
                      'explanation': 'list.append(x) appends an item to the end of the list in place.',
                      'option_a': 'insert_end()',
                      'option_b': 'push()',
                      'option_c': 'append()',
                      'option_d': 'add()',
                      'question_text': 'Which method is used to add a new item to the end of an existing list in '
                                       'Python?'},
                  {   'correct_option': 'C',
                      'explanation': "Dictionaries ('dict') store mappings of unique keys to values using curly braces "
                                     "(e.g. {'score': 100}).",
                      'option_a': 'Array',
                      'option_b': 'Tuple',
                      'option_c': 'Dictionary',
                      'option_d': 'List',
                      'question_text': 'Which built-in type represents key-value pairs enclosed in curly braces {} in '
                                       'Python?'},
                  {   'correct_option': 'B',
                      'explanation': "In Python, 0, empty sequences ('', [], {}), and None evaluate to False in a "
                                     'boolean context.',
                      'option_a': 'Error',
                      'option_b': 'False',
                      'option_c': 'True',
                      'option_d': 'None',
                      'question_text': 'What is the boolean evaluation of bool(0) in Python?'},
                  {   'correct_option': 'B',
                      'explanation': "'=' is the assignment operator, whereas '==' compares two values for equality.",
                      'option_a': '=',
                      'option_b': '==',
                      'option_c': '===',
                      'option_d': 'equals',
                      'question_text': 'Which operator is used to check if two values are equal in Python?'},
                  {   'correct_option': 'D',
                      'explanation': "The 'break' statement terminates the nearest enclosing loop prematurely.",
                      'option_a': 'Restarts the loop from index 0',
                      'option_b': 'Pauses execution for 1 second',
                      'option_c': 'Skips the current iteration and goes to next',
                      'option_d': 'Exits the loop immediately',
                      'question_text': "What does the 'break' keyword do inside a while or for loop in Python?"},
                  {   'correct_option': 'B',
                      'explanation': "The 'return' statement exits a function and optionally passes an expression back "
                                     'to the caller.',
                      'option_a': 'yield_result',
                      'option_b': 'return',
                      'option_c': 'send',
                      'option_d': 'output',
                      'question_text': 'Which keyword is used to return a result from a Python function?'},
                  {   'correct_option': 'D',
                      'explanation': 'The built-in int() constructor parses a valid string representation of a whole '
                                     'number into an integer.',
                      'option_a': 'str.to_int("150")',
                      'option_b': 'parse("150")',
                      'option_c': 'integer("150")',
                      'option_d': 'int("150")',
                      'question_text': 'How can you convert the string "150" into an integer in Python?'},
                  {   'correct_option': 'C',
                      'explanation': 'Tuples (defined with parentheses) cannot be modified after creation, making them '
                                     'immutable.',
                      'option_a': 'List',
                      'option_b': 'Dictionary',
                      'option_c': 'Tuple',
                      'option_d': 'Set',
                      'question_text': 'Which of the following is an IMMUTABLE sequence type in Python?'},
                  {   'correct_option': 'D',
                      'explanation': "The logical operator 'not' inverts the truth value, so 'not True' evaluates to "
                                     'False.',
                      'option_a': 'True',
                      'option_b': 'None',
                      'option_c': '0',
                      'option_d': 'False',
                      'question_text': "What does the expression 'not True' evaluate to in Python?"},
                  {   'correct_option': 'A',
                      'explanation': 'Strings in Python support zero-based indexing. Index 0 accesses the first '
                                     "character, 'P'.",
                      'option_a': 'P',
                      'option_b': 'Python',
                      'option_c': 'y',
                      'option_d': 'IndexError',
                      'question_text': 'What will be printed by: print("Python"[0])?'}],
    'science': [   {   'correct_option': 'B',
                       'explanation': 'Mitochondria generate most of the chemical energy required by the cell through '
                                      'cellular respiration, producing ATP.',
                       'option_a': 'Ribosome',
                       'option_b': 'Mitochondria',
                       'option_c': 'Nucleus',
                       'option_d': 'Golgi apparatus',
                       'question_text': 'What is the powerhouse organelle of a eukaryotic cell responsible for '
                                        'generating ATP energy?'},
                   {   'correct_option': 'B',
                       'explanation': 'The speed of light in a vacuum (c) is approximately 3 × 10^8 m/s, or 300,000 '
                                      'kilometers per second.',
                       'option_a': '150,000 km/s',
                       'option_b': '300,000 km/s',
                       'option_c': '1,000,000 km/s',
                       'option_d': '30,000 km/s',
                       'question_text': 'What is the approximate speed of light in a vacuum?'},
                   {   'correct_option': 'C',
                       'explanation': "Gold has the chemical symbol 'Au', originating from the Latin word 'Aurum' "
                                      'meaning shining dawn.',
                       'option_a': 'Ag',
                       'option_b': 'Fe',
                       'option_c': 'Au',
                       'option_d': 'Gd',
                       'question_text': 'What is the chemical symbol for the element Gold on the Periodic Table?'},
                   {   'correct_option': 'D',
                       'explanation': 'Mars appears reddish because of the high abundance of ferric oxide (rust) in '
                                      'its soil and atmosphere.',
                       'option_a': 'Saturn',
                       'option_b': 'Jupiter',
                       'option_c': 'Venus',
                       'option_d': 'Mars',
                       'question_text': "Which planet in our solar system is known as the 'Red Planet' due to iron "
                                        'oxide on its surface?'},
                   {   'correct_option': 'C',
                       'explanation': "Newton's Third Law of Motion states that whenever an object exerts a force on "
                                      'another, the second exerts an equal force in the opposite direction.',
                       'option_a': 'Law of Conservation of Energy',
                       'option_b': "Newton's First Law",
                       'option_c': "Newton's Third Law",
                       'option_d': "Newton's Second Law",
                       'question_text': "Which law of physics states that 'For every action, there is an equal and "
                                        "opposite reaction'?"},
                   {   'correct_option': 'A',
                       'explanation': 'Plants take in carbon dioxide and water in the presence of sunlight and '
                                      'chlorophyll to produce glucose and release oxygen.',
                       'option_a': 'Carbon Dioxide (CO2)',
                       'option_b': 'Methane',
                       'option_c': 'Nitrogen',
                       'option_d': 'Oxygen',
                       'question_text': 'What gas do green plants primarily absorb from the atmosphere during '
                                        'photosynthesis?'},
                   {   'correct_option': 'B',
                       'explanation': 'A pH of 7 represents neutral acidity/alkalinity. Values below 7 are acidic, '
                                      'while values above 7 are basic/alkaline.',
                       'option_a': '9',
                       'option_b': '7',
                       'option_c': '5',
                       'option_d': '0',
                       'question_text': 'What is the pH value of pure distilled water at 25 degrees Celsius, '
                                        'representing neutral pH?'},
                   {   'correct_option': 'A',
                       'explanation': 'Electrons carry a negative charge (-1), protons carry a positive charge (+1), '
                                      'and neutrons have no charge (neutral).',
                       'option_a': 'Electron',
                       'option_b': 'Positron',
                       'option_c': 'Proton',
                       'option_d': 'Neutron',
                       'question_text': 'Which fundamental particle of an atom carries a negative electrical charge?'},
                   {   'correct_option': 'C',
                       'explanation': 'Sir Alexander Fleming discovered penicillin from Penicillium notatum mold at '
                                      "St. Mary's Hospital in London in 1928.",
                       'option_a': 'Louis Pasteur',
                       'option_b': 'Robert Koch',
                       'option_c': 'Alexander Fleming',
                       'option_d': 'Edward Jenner',
                       'question_text': 'Who discovered the first effective antibiotic, Penicillin, in 1928?'},
                   {   'correct_option': 'D',
                       'explanation': 'The SI unit of electrical resistance is the Ohm (symbol: Ω), named after German '
                                      'physicist Georg Simon Ohm.',
                       'option_a': 'Ampere',
                       'option_b': 'Watt',
                       'option_c': 'Volt',
                       'option_d': 'Ohm (Ω)',
                       'question_text': 'What is the SI unit of electrical resistance?'},
                   {   'correct_option': 'D',
                       'explanation': "Earth's dry atmosphere is composed of approximately 78.08% Nitrogen and 20.95% "
                                      'Oxygen.',
                       'option_a': 'Oxygen (~21%)',
                       'option_b': 'Carbon Dioxide (~0.04%)',
                       'option_c': 'Argon (~0.93%)',
                       'option_d': 'Nitrogen (~78%)',
                       'question_text': "Which gas is most abundant by volume in the Earth's atmosphere?"},
                   {   'correct_option': 'A',
                       'explanation': 'Table salt is Sodium Chloride, formed by the ionic bonding of sodium (Na) and '
                                      'chlorine (Cl), with formula NaCl.',
                       'option_a': 'NaCl',
                       'option_b': 'KCl',
                       'option_c': 'CaCl2',
                       'option_d': 'NaHCO3',
                       'question_text': 'What is the chemical formula of common table salt?'},
                   {   'correct_option': 'D',
                       'explanation': 'Jupiter is the largest planet, with a mass more than two and a half times that '
                                      'of all other planets combined.',
                       'option_a': 'Uranus',
                       'option_b': 'Saturn',
                       'option_c': 'Neptune',
                       'option_d': 'Jupiter',
                       'question_text': 'Which planet is the largest in our solar system by both diameter and mass?'},
                   {   'correct_option': 'C',
                       'explanation': 'Red Blood Cells contain hemoglobin, an iron-rich protein that binds oxygen and '
                                      'delivers it throughout the body.',
                       'option_a': 'Platelets (Thrombocytes)',
                       'option_b': 'Plasma cells',
                       'option_c': 'Red Blood Cells (Erythrocytes)',
                       'option_d': 'White Blood Cells (Leukocytes)',
                       'question_text': 'Which blood cells are responsible for carrying oxygen from the lungs to body '
                                        'tissues?'},
                   {   'correct_option': 'B',
                       'explanation': 'A concave lens is thicker at edges and thinner in center, causing incident rays '
                                      'to diverge outward.',
                       'option_a': 'Convex lens',
                       'option_b': 'Concave lens',
                       'option_c': 'Cylindrical lens',
                       'option_d': 'Bifocal lens',
                       'question_text': 'What type of lens is thinner in the middle and causes parallel rays of light '
                                        'to diverge?'},
                   {   'correct_option': 'B',
                       'explanation': 'Ozone is a triatomic molecule made of three oxygen atoms (O3) that absorbs '
                                      'harmful ultraviolet (UV) radiation.',
                       'option_a': 'O2',
                       'option_b': 'O3',
                       'option_c': 'CO2',
                       'option_d': 'H2O2',
                       'question_text': 'What is the molecular formula for Ozone gas present in the stratosphere?'},
                   {   'correct_option': 'A',
                       'explanation': 'At 1 atmosphere of pressure, water boils at 100 °C (or 212 °F / 373.15 K).',
                       'option_a': '100 °C',
                       'option_b': '50 °C',
                       'option_c': '212 °C',
                       'option_d': '0 °C',
                       'question_text': 'What is the boiling point of pure water at standard atmospheric pressure in '
                                        'Celsius?'},
                   {   'correct_option': 'A',
                       'explanation': 'Albert Einstein published the Special Theory of Relativity (1905) and General '
                                      'Relativity (1915), reshaping modern physics.',
                       'option_a': 'Albert Einstein',
                       'option_b': 'Galileo Galilei',
                       'option_c': 'Isaac Newton',
                       'option_d': 'Niels Bohr',
                       'question_text': 'Who formulated the Theory of General Relativity and the equation E = mc²?'},
                   {   'correct_option': 'B',
                       'explanation': 'The beta cells of the Islets of Langerhans in the pancreas secrete insulin to '
                                      'facilitate glucose uptake.',
                       'option_a': 'Kidney',
                       'option_b': 'Pancreas',
                       'option_c': 'Stomach',
                       'option_d': 'Liver',
                       'question_text': 'Which organ in the human body produces the hormone Insulin to regulate blood '
                                        'sugar levels?'},
                   {   'correct_option': 'C',
                       'explanation': 'The SI unit of force is the Newton (N), defined as 1 kg·m/s².',
                       'option_a': 'Watt',
                       'option_b': 'Joule',
                       'option_c': 'Newton (N)',
                       'option_d': 'Pascal',
                       'question_text': 'What is the SI unit of Force?'},
                   {   'correct_option': 'D',
                       'explanation': 'The crystalline lens, controlled by ciliary muscles, changes shape '
                                      '(accommodation) to focus objects at various distances.',
                       'option_a': 'Iris',
                       'option_b': 'Cornea',
                       'option_c': 'Pupil',
                       'option_d': 'Crystalline Lens',
                       'question_text': 'Which component of the human eye adjusts its curvature to focus images on the '
                                        'retina?'},
                   {   'correct_option': 'A',
                       'explanation': 'Sublimation is the direct transition from solid to gaseous state, as observed '
                                      'in dry ice (solid CO2) and camphor.',
                       'option_a': 'Sublimation',
                       'option_b': 'Evaporation',
                       'option_c': 'Condensation',
                       'option_d': 'Deposition',
                       'question_text': 'What is the process called when a solid turns directly into a gas without '
                                        'passing through a liquid state?'}]}


def seed_database(db_manager):
    """
    Seeds the database with categories and questions.
    Works with either MySQL or SQLite database manager.
    """
    print("[INFO] Starting database seed process...")
    
    # 1. Insert Categories
    category_id_map = {}
    for cat in CATEGORIES:
        existing = db_manager.execute_query(
            "SELECT id FROM categories WHERE code = %s OR name = %s",
            (cat["code"], cat["name"]),
            fetch_one=True
        )
        if existing:
            cat_id = existing["id"] if isinstance(existing, dict) else existing[0]
            print(f" -> Category '{cat['name']}' already exists (ID: {cat_id})")
        else:
            cat_id = db_manager.execute_insert(
                "INSERT INTO categories (name, code, description, icon) VALUES (%s, %s, %s, %s)",
                (cat["name"], cat["code"], cat["description"], cat["icon"])
            )
            print(f" -> Created category '{cat['name']}' (ID: {cat_id})")
        category_id_map[cat["code"]] = cat_id

    # 2. Insert Questions
    total_added = 0
    total_existing = 0

    for code, q_list in QUESTIONS.items():
        cat_id = category_id_map.get(code)
        if not cat_id:
            print(f"[WARN] Category code '{code}' not mapped. Skipping.")
            continue
            
        for q in q_list:
            # Check if duplicate question already in this category
            existing_q = db_manager.execute_query(
                "SELECT id FROM questions WHERE category_id = %s AND question_text = %s",
                (cat_id, q["question_text"]),
                fetch_one=True
            )
            if existing_q:
                total_existing += 1
                continue
                
            db_manager.execute_insert(
                """INSERT INTO questions 
                   (category_id, question_text, option_a, option_b, option_c, option_d, correct_option, explanation) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    cat_id,
                    q["question_text"],
                    q["option_a"],
                    q["option_b"],
                    q["option_c"],
                    q["option_d"],
                    q["correct_option"],
                    q["explanation"]
                )
            )
            total_added += 1

    print(f"[SUCCESS] Seed complete! Added: {total_added} questions, Skipped (already existed): {total_existing} questions.")
    return total_added
