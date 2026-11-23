# -*- coding: utf-8 -*-
"""Contenido bilingüe del sitio (original). Edita aquí los textos.

Regla: sin cifras, certificaciones, reseñas ni premios inventados.
Los únicos "datos" usados son compromisos operativos que el negocio debe
confirmar (respuesta en 1 día hábil, solicitudes 24/7, atención EN/ES).
"""

# ---------------------------------------------------------------- servicios
SERVICES = [
    {
        "id": "office",
        "slug": {"en": "office-cleaning", "es": "limpieza-de-oficinas"},
        "img": "service-office",
        "en": {
            "name": "Office Cleaning",
            "short": "Recurring cleaning for offices, coworking spaces and professional suites.",
            "tagline": "A tidy workplace, on a routine that fits your team.",
            "meta_title": "Office Cleaning Services in the Midwest | ABC Midwest",
            "meta_desc": "Recurring office cleaning for workplaces across the Midwest. Custom scope, flexible schedules and a written quote within 1 business day.",
            "img_alt": "Clean, bright open-plan office with desks and daylight",
            "summary": [
                "Office cleaning keeps shared spaces, workstations and restrooms in order so your team can focus on work. We build a checklist around how your space is actually used, then repeat it on a schedule you choose.",
                "Every plan starts with a conversation about your layout, hours and priorities. The scope, frequency and price are written in your quote, so there are no surprises."
            ],
            "includes": [
                ["Workstations and common areas", "Dusting, wiping and tidying of desks, meeting rooms, break areas and reception."],
                ["Restrooms and kitchenettes", "Cleaning and disinfecting of fixtures, counters and high-touch surfaces, plus restocking if agreed."],
                ["Floors and entrances", "Vacuuming, sweeping and mopping, with attention to entry mats and walk-off areas."],
                ["Trash and recycling", "Collection and liner replacement on the schedule defined in your plan."]
            ],
            "faqs": [
                ["How often can you clean our office?", "Plans can be daily, several times a week, weekly or on another rhythm. We agree on the frequency during the quote."],
                ["Can the cleaning happen outside business hours?", "Yes. We plan service windows around your operations, including early or late hours when your building allows it."],
                ["Do I need to sign a long contract?", "Terms are set in the written proposal. Tell us what you prefer and we will include it in the quote."]
            ]
        },
        "es": {
            "name": "Limpieza de oficinas",
            "short": "Limpieza recurrente para oficinas, espacios de coworking y consultorios profesionales.",
            "tagline": "Un lugar de trabajo ordenado, con una rutina que se adapta a su equipo.",
            "meta_title": "Limpieza de oficinas en el Medio Oeste | ABC Midwest",
            "meta_desc": "Limpieza recurrente de oficinas en el Medio Oeste. Alcance a medida, horarios flexibles y cotización por escrito en 1 día hábil.",
            "img_alt": "Oficina abierta, limpia y luminosa con escritorios y luz natural",
            "summary": [
                "La limpieza de oficinas mantiene en orden las áreas comunes, los puestos de trabajo y los baños para que su equipo se concentre en lo importante. Armamos una lista de tareas según el uso real de su espacio y la repetimos con la frecuencia que usted elija.",
                "Cada plan empieza con una conversación sobre su distribución, horarios y prioridades. El alcance, la frecuencia y el precio quedan por escrito en la cotización, sin sorpresas."
            ],
            "includes": [
                ["Puestos de trabajo y áreas comunes", "Quitar el polvo, limpiar y ordenar escritorios, salas de reuniones, áreas de descanso y recepción."],
                ["Baños y cocinetas", "Limpieza y desinfección de accesorios, mesones y superficies de alto contacto, con reposición de insumos si se acuerda."],
                ["Pisos y entradas", "Aspirado, barrido y trapeado, con atención a tapetes de entrada y zonas de mayor tránsito."],
                ["Basura y reciclaje", "Retiro y cambio de bolsas según el calendario definido en su plan."]
            ],
            "faqs": [
                ["¿Con qué frecuencia pueden limpiar nuestra oficina?", "Los planes pueden ser diarios, varias veces por semana, semanales o con otro ritmo. Acordamos la frecuencia durante la cotización."],
                ["¿Se puede limpiar fuera del horario de oficina?", "Sí. Planificamos las ventanas de servicio según su operación, incluyendo horas tempranas o tardías cuando su edificio lo permita."],
                ["¿Debo firmar un contrato largo?", "Las condiciones se definen en la propuesta escrita. Cuéntenos qué prefiere y lo incluiremos en la cotización."]
            ]
        }
    },
    {
        "id": "post",
        "slug": {"en": "post-construction-cleaning", "es": "limpieza-post-construccion"},
        "img": "service-post",
        "en": {
            "name": "Post-Construction Cleaning",
            "short": "Detailed cleanup after build-outs and renovations, so the space is ready to open.",
            "tagline": "From dust and debris to a space ready for its first day.",
            "meta_title": "Post-Construction Cleaning in the Midwest | ABC Midwest",
            "meta_desc": "Post-construction and renovation cleanup for commercial spaces in the Midwest. Request a free written quote and we reply within 1 business day.",
            "img_alt": "Newly renovated commercial interior being cleaned after construction",
            "summary": [
                "After a build-out or renovation, fine dust settles on every surface. Post-construction cleaning removes debris and residue so the space can be inspected, furnished and opened.",
                "The scope depends on the size and condition of the project. We review the details with you and put the stages, access needs and price in writing."
            ],
            "includes": [
                ["Debris and dust removal", "Removal of loose debris and fine dust from floors, ledges, vents accessible without tools and built-in surfaces."],
                ["Surfaces and fixtures", "Cleaning of counters, cabinets, doors, trim and installed fixtures, including sticker and residue removal where safe."],
                ["Glass and frames", "Interior glass, mirrors and window frames cleaned and checked for streaks."],
                ["Final detail pass", "A last walk-through pass to touch up details before hand-over."]
            ],
            "faqs": [
                ["When should post-construction cleaning be scheduled?", "Usually after the contractor finishes the main work and before furniture or operations move in. We coordinate timing with your project schedule."],
                ["Do you handle construction waste removal?", "Bulk construction waste and hazardous materials are normally handled by the contractor. We will confirm what is and is not covered in your quote."],
                ["Can the cleaning be done in stages?", "Yes. Rough, final and touch-up cleans can be planned as separate visits if the project needs it."]
            ]
        },
        "es": {
            "name": "Limpieza post-construcción",
            "short": "Limpieza detallada después de remodelaciones y obras, para dejar el espacio listo para abrir.",
            "tagline": "Del polvo y los escombros a un espacio listo para su primer día.",
            "meta_title": "Limpieza post-construcción en el Medio Oeste | ABC Midwest",
            "meta_desc": "Limpieza posterior a obras y remodelaciones para espacios comerciales en el Medio Oeste. Cotización gratis por escrito en 1 día hábil.",
            "img_alt": "Interior comercial recién remodelado durante la limpieza posterior a la obra",
            "summary": [
                "Después de una obra o remodelación, el polvo fino se deposita en todas las superficies. La limpieza post-construcción retira residuos y restos para que el espacio pueda inspeccionarse, amoblarse y abrir.",
                "El alcance depende del tamaño y del estado del proyecto. Revisamos los detalles con usted y dejamos por escrito las etapas, los accesos necesarios y el precio."
            ],
            "includes": [
                ["Retiro de residuos y polvo", "Retiro de residuos sueltos y polvo fino en pisos, repisas, rejillas accesibles sin herramientas y superficies fijas."],
                ["Superficies y accesorios", "Limpieza de mesones, gabinetes, puertas, molduras y accesorios instalados, retirando etiquetas y residuos cuando es seguro."],
                ["Vidrios y marcos", "Vidrios interiores, espejos y marcos de ventanas limpios y revisados."],
                ["Revisión final de detalles", "Una pasada final de retoques antes de la entrega del espacio."]
            ],
            "faqs": [
                ["¿Cuándo se programa la limpieza post-construcción?", "Normalmente cuando el contratista termina la obra principal y antes de que entren muebles u operaciones. Coordinamos los tiempos con el cronograma de su proyecto."],
                ["¿Retiran los escombros de la obra?", "Los escombros voluminosos y los materiales peligrosos suelen ser responsabilidad del contratista. Confirmaremos en su cotización qué incluye y qué no."],
                ["¿Se puede hacer por etapas?", "Sí. La limpieza gruesa, la final y los retoques pueden planificarse como visitas separadas si el proyecto lo requiere."]
            ]
        }
    },
    {
        "id": "floors",
        "slug": {"en": "floor-care", "es": "cuidado-de-pisos"},
        "img": "service-floors",
        "en": {
            "name": "Floor Care",
            "short": "Machine scrubbing, buffing and recoating plans for commercial flooring.",
            "tagline": "Floors that look maintained, from the lobby to the back room.",
            "meta_title": "Commercial Floor Care Services in the Midwest | ABC Midwest",
            "meta_desc": "Commercial floor care in the Midwest: machine scrubbing, buffing and periodic maintenance plans. Request a free quote; we reply in 1 business day.",
            "img_alt": "Polished commercial floor in a bright lobby",
            "summary": [
                "Floors take the most wear in any building and are the first thing visitors notice. Floor care goes beyond daily mopping, using equipment and methods suited to each surface.",
                "We assess the flooring type and its condition, then recommend a plan, one-time or recurring, and write it into your quote."
            ],
            "includes": [
                ["Machine scrubbing", "Deep cleaning of hard floors to lift embedded dirt that routine mopping leaves behind."],
                ["Buffing and finish care", "Buffing and, where suitable for the floor, finish application to protect and refresh the surface."],
                ["Carpet maintenance", "Vacuuming and extraction cleaning for carpeted areas, with spot treatment on request."],
                ["Maintenance schedule", "A periodic plan so floor care happens before wear becomes visible."]
            ],
            "faqs": [
                ["What types of flooring do you work with?", "Common commercial surfaces such as vinyl, tile, sealed concrete and carpet. Tell us what you have and we will confirm the right method."],
                ["Will the area be closed during floor care?", "Some treatments need dry time. We plan the work for low-traffic periods and tell you in advance which areas need to stay clear."],
                ["Is floor care a one-time or recurring service?", "Either. Many sites combine routine cleaning with periodic deep floor care."]
            ]
        },
        "es": {
            "name": "Cuidado de pisos",
            "short": "Planes de lavado con máquina, pulido y renovación de acabado para pisos comerciales.",
            "tagline": "Pisos que se ven bien cuidados, del vestíbulo a la bodega.",
            "meta_title": "Cuidado de pisos comerciales en el Medio Oeste | ABC Midwest",
            "meta_desc": "Cuidado de pisos comerciales en el Medio Oeste: lavado con máquina, pulido y planes de mantenimiento. Cotización gratis en 1 día hábil.",
            "img_alt": "Piso comercial pulido en un vestíbulo luminoso",
            "summary": [
                "Los pisos soportan el mayor desgaste de cualquier edificio y son lo primero que ven las visitas. El cuidado de pisos va más allá del trapeado diario, con equipos y métodos adecuados para cada superficie.",
                "Evaluamos el tipo de piso y su estado, y le recomendamos un plan, puntual o recurrente, que dejamos por escrito en su cotización."
            ],
            "includes": [
                ["Lavado con máquina", "Limpieza profunda de pisos duros para retirar la suciedad incrustada que el trapeado rutinario no alcanza."],
                ["Pulido y cuidado del acabado", "Pulido y, cuando el piso lo permite, aplicación de acabado para proteger y renovar la superficie."],
                ["Mantenimiento de alfombras", "Aspirado y limpieza por extracción en áreas alfombradas, con tratamiento de manchas a solicitud."],
                ["Calendario de mantenimiento", "Un plan periódico para actuar antes de que el desgaste sea visible."]
            ],
            "faqs": [
                ["¿Con qué tipos de piso trabajan?", "Superficies comerciales comunes como vinilo, baldosa, concreto sellado y alfombra. Cuéntenos qué tiene y confirmaremos el método adecuado."],
                ["¿Se cierra el área durante el trabajo?", "Algunos tratamientos requieren tiempo de secado. Programamos el trabajo en horas de poco tránsito y le avisamos qué zonas deben quedar libres."],
                ["¿Es un servicio puntual o recurrente?", "Ambos. Muchos sitios combinan la limpieza de rutina con cuidado profundo de pisos de forma periódica."]
            ]
        }
    },
    {
        "id": "windows",
        "slug": {"en": "window-cleaning", "es": "limpieza-de-ventanas"},
        "img": "service-windows",
        "en": {
            "name": "Window Cleaning",
            "short": "Interior and exterior glass cleaning for storefronts and office buildings.",
            "tagline": "Clear glass that lets daylight, and your brand, show through.",
            "meta_title": "Commercial Window Cleaning in the Midwest | ABC Midwest",
            "meta_desc": "Interior and exterior window cleaning for storefronts and offices in the Midwest. Free written quote with a reply within 1 business day.",
            "img_alt": "Clean glass storefront and office windows reflecting daylight",
            "summary": [
                "Clean windows improve how a storefront or office looks from the street and how it feels inside. We clean glass, frames and sills on a one-time or recurring basis.",
                "Access and height determine the method and the price, so we confirm those details with you and put the scope in writing."
            ],
            "includes": [
                ["Storefront glass", "Streak-free cleaning of entrance doors and display windows."],
                ["Interior and exterior panes", "Both sides of accessible glass, with frames and sills wiped down."],
                ["Partitions and mirrors", "Interior glass walls, partitions and mirrors."],
                ["Seasonal or recurring plans", "A calendar that fits your building, weather and how often the glass needs attention."]
            ],
            "faqs": [
                ["Do you clean exterior windows on upper floors?", "Access depends on the building. Tell us the number of floors and how the windows can be reached, and we will confirm what we can quote."],
                ["Does weather affect the schedule?", "Exterior work can be rescheduled in rain, ice or high wind. We will coordinate a new date with you."],
                ["Can window cleaning be added to a cleaning plan?", "Yes. It can be bundled with other services in a single proposal."]
            ]
        },
        "es": {
            "name": "Limpieza de ventanas",
            "short": "Limpieza de vidrios interiores y exteriores para locales y edificios de oficinas.",
            "tagline": "Vidrios claros que dejan pasar la luz y también la imagen de su marca.",
            "meta_title": "Limpieza de ventanas comerciales en el Medio Oeste | ABC Midwest",
            "meta_desc": "Limpieza de ventanas interiores y exteriores para locales y oficinas en el Medio Oeste. Cotización gratis por escrito en 1 día hábil.",
            "img_alt": "Vidrios de local y oficina limpios que reflejan la luz del día",
            "summary": [
                "Las ventanas limpias mejoran cómo se ve un local u oficina desde la calle y cómo se siente por dentro. Limpiamos vidrios, marcos y repisas de forma puntual o recurrente.",
                "El acceso y la altura determinan el método y el precio, por eso confirmamos esos detalles con usted y dejamos el alcance por escrito."
            ],
            "includes": [
                ["Vidrios de fachada", "Limpieza sin vetas de puertas de entrada y vitrinas."],
                ["Paneles interiores y exteriores", "Ambos lados de los vidrios accesibles, con marcos y repisas limpios."],
                ["Divisiones y espejos", "Paredes de vidrio interiores, divisiones y espejos."],
                ["Planes estacionales o recurrentes", "Un calendario ajustado a su edificio, al clima y a la frecuencia que necesite."]
            ],
            "faqs": [
                ["¿Limpian ventanas exteriores en pisos altos?", "El acceso depende del edificio. Indíquenos cuántos pisos tiene y cómo se llega a las ventanas, y confirmaremos qué podemos cotizar."],
                ["¿El clima afecta la programación?", "El trabajo exterior puede reprogramarse por lluvia, hielo o viento fuerte. Acordaremos con usted una nueva fecha."],
                ["¿Puedo agregar ventanas a un plan de limpieza?", "Sí. Puede combinarse con otros servicios en una sola propuesta."]
            ]
        }
    },
    {
        "id": "daily",
        "slug": {"en": "day-porter-service", "es": "mantenimiento-diario"},
        "img": "service-daily",
        "en": {
            "name": "Day Porter Service",
            "short": "On-site upkeep during business hours: restrooms, lobbies and shared areas.",
            "tagline": "Shared spaces kept presentable while your doors are open.",
            "meta_title": "Day Porter & On-Site Upkeep Services | ABC Midwest",
            "meta_desc": "Day porter service for buildings and facilities in the Midwest: restroom checks, lobby upkeep and more. Free quote, reply in 1 business day.",
            "img_alt": "Clean building lobby with a reception area during the day",
            "summary": [
                "A day porter looks after high-traffic areas while the building is in use, handling the small things that cannot wait for the evening clean.",
                "Coverage hours and tasks are tailored to your site and written into the quote, from a few hours a day to a full schedule."
            ],
            "includes": [
                ["Restroom checks", "Regular checks, wipe-downs and restocking of supplies during the day."],
                ["Lobby and entrance upkeep", "Keeping reception areas, entry glass and walkways presentable."],
                ["Breakroom and common areas", "Tidying shared kitchens, meeting rooms and seating areas between uses."],
                ["Spills and quick response", "On-site attention to spills, trash and similar needs as they come up."]
            ],
            "faqs": [
                ["How many hours of coverage can we choose?", "Coverage is defined by your needs, from a few hours to a full day. We set it in the quote."],
                ["Is a day porter the same as evening cleaning?", "No. Day porter service maintains the space during business hours and complements, rather than replaces, a regular cleaning plan."],
                ["Can the same team handle both services?", "We can propose both services together so they are planned as one routine."]
            ]
        },
        "es": {
            "name": "Mantenimiento diario en sitio",
            "short": "Atención en sitio durante el horario laboral: baños, vestíbulos y áreas comunes.",
            "tagline": "Áreas comunes presentables mientras su negocio está abierto.",
            "meta_title": "Mantenimiento diario en sitio y conserjería | ABC Midwest",
            "meta_desc": "Servicio de mantenimiento diario en edificios e instalaciones del Medio Oeste: baños, vestíbulos y más. Cotización gratis en 1 día hábil.",
            "img_alt": "Vestíbulo de edificio limpio con área de recepción durante el día",
            "summary": [
                "Un auxiliar de mantenimiento diario atiende las zonas de mayor tránsito mientras el edificio está en uso y resuelve lo que no puede esperar a la limpieza de la noche.",
                "Las horas de cobertura y las tareas se adaptan a su sitio y quedan en la cotización, desde pocas horas al día hasta un horario completo."
            ],
            "includes": [
                ["Revisión de baños", "Revisiones periódicas, limpieza rápida y reposición de insumos durante el día."],
                ["Vestíbulo y entradas", "Mantener recepción, vidrios de entrada y accesos presentables."],
                ["Cocinetas y áreas comunes", "Ordenar cocinas compartidas, salas de reuniones y zonas de descanso entre usos."],
                ["Derrames y respuesta rápida", "Atención en sitio de derrames, basura y necesidades similares cuando surgen."]
            ],
            "faqs": [
                ["¿Cuántas horas de cobertura podemos elegir?", "La cobertura se define según sus necesidades, desde pocas horas hasta una jornada completa. La fijamos en la cotización."],
                ["¿Es lo mismo que la limpieza nocturna?", "No. El mantenimiento diario cuida el espacio en horario laboral y complementa, sin reemplazar, un plan de limpieza regular."],
                ["¿El mismo equipo puede encargarse de ambos?", "Podemos proponer ambos servicios juntos para planificarlos como una sola rutina."]
            ]
        }
    },
]

# --------------------------------------------------------- cadenas de la UI
UI = {
    "en": {
        "lang_name": "English", "lang_code": "EN", "html_lang": "en", "og_locale": "en_US",
        "home_h1": "Commercial cleaning for Midwest businesses",
        "about_img_alt": "Cleaning team preparing a commercial space",
        "skip": "Skip to main content",
        "nav_home": "Home", "nav_services": "Services", "nav_about": "About", "nav_contact": "Contact",
        "menu": "Menu", "close": "Close", "all_services": "All services",
        "cta_quote": "Get a quote", "cta_call": "Call", "cta_whatsapp": "WhatsApp us",
        "call_us": "Call us", "email_us": "Email us", "learn_more": "Learn more",
        "primary_nav": "Main navigation", "language": "Language", "switch_to": "Español",
        "prev": "Previous slide", "next": "Next slide", "pause": "Pause slideshow", "play": "Play slideshow",
        "go_slide": "Go to slide",
        "breadcrumb": "Breadcrumb",
        "facts": [
            ["1 day", "Business-day response to quote requests"],
            ["24/7", "Online quote requests, any time"],
            ["EN / ES", "Service in English and Spanish"],
            ["Free", "Written, no-obligation quotes"],
        ],
        "services_eyebrow": "What we do", "services_title": "Commercial cleaning services",
        "services_lead": "Choose a service or tell us what your space needs and we will build the plan around it.",
        "process_eyebrow": "How it works", "process_title": "From first message to a cleaner space",
        "process": [
            ["Tell us about your space", "Send a short request with your property type, location and the service you need."],
            ["We review the details", "We confirm the scope with you and, when needed, review the site."],
            ["Receive a written quote", "Scope, frequency and price in writing, within 1 business day of your request."],
            ["Service begins", "We start on the agreed schedule and stay in touch to adjust the plan as needed."],
        ],
        "about_eyebrow": "About us", "about_title": "A cleaning partner that communicates clearly",
        "about_text": [
            "ABC Midwest Commercial Cleaning supports offices, retail spaces and facilities with dependable cleaning plans. We keep the process simple: you tell us what you need, we put the plan in writing, and we follow it.",
            "We serve clients in English and Spanish, so your whole team can talk to us in the language they are most comfortable with."
        ],
        "about_cta": "More about us",
        "areas_title": "Service areas",
        "areas_lead": "We provide commercial cleaning in the following states. If you are nearby, ask us.",
        "faq_eyebrow": "FAQ", "faq_title": "Frequently asked questions",
        "faq_home": [
            ["What types of properties do you clean?", "We work with offices, retail spaces, professional suites, the office areas of warehouses and other commercial properties. If yours is different, tell us and we will let you know if we can help."],
            ["How do I get a quote?", "Use the quote form or call us. We confirm the scope with you and send a written quote within 1 business day."],
            ["Do you offer one-time and recurring cleaning?", "Both. Recurring plans are set by frequency and one-time services by scope, and both are detailed in your quote."],
            ["Do you speak Spanish?", "Yes. We communicate in English and Spanish, and this website is available in both."],
            ["Which areas do you serve?", "We serve the Midwest states listed in our service areas. Contact us if you are unsure whether your location is covered."],
        ],
        "banner_title": "Ready for a cleaner workplace?",
        "banner_text": "Tell us about your space and get a written quote within 1 business day.",
        "trust": ["Free written quote", "Reply in 1 business day", "English and Spanish"],
        "includes_title": "What is included",
        "includes_lead": "The exact scope is confirmed in your written quote. Typical tasks include:",
        "process_service_title": "How we work",
        "faq_service_title": "Questions about this service",
        "quote_card_title": "Request a free quote",
        "quote_card_text": "Tell us about your space and we will reply within 1 business day.",
        "other_services": "Other services",
        "services_page_title": "Our services",
        "services_page_h1": "Commercial cleaning services",
        "services_page_lead": "Reliable cleaning for the places where business happens.",
        "services_meta_title": "Commercial Cleaning Services in the Midwest | ABC Midwest",
        "services_meta_desc": "Office, post-construction, floor, window and day porter cleaning for Midwest businesses. Free written quote within 1 business day.",
        "home_meta_title": "Commercial Cleaning in the Midwest | ABC Midwest",
        "home_meta_desc": "Commercial cleaning for offices and facilities across the Midwest. English and Spanish service, free written quote within 1 business day.",
        "slides": [
            ["Clean spaces for productive days", "Commercial cleaning for offices, retail and facilities across the Midwest.", "hero-1", "Bright, tidy commercial office interior"],
            ["Planned around your schedule", "We set service windows that work with your operations, not against them.", "hero-2", "Cleaning team member maintaining a commercial lobby floor"],
            ["Request a quote in minutes", "Share a few details and receive a written quote within 1 business day.", "hero-3", "Clean modern building exterior with glass windows"],
        ],
        "about_meta_title": "About ABC Midwest | Commercial Cleaning Company",
        "about_meta_desc": "Learn how ABC Midwest approaches commercial cleaning: clear communication, written plans and service in English and Spanish.",
        "about_h1": "About ABC Midwest",
        "about_lead": "Commercial cleaning built on clear plans and clear communication.",
        "about_body": [
            "We started from a simple idea: a cleaning service should be easy to talk to and easy to hold to its word. That is why every engagement begins with a written scope that both sides understand.",
            "Our work covers offices, retail spaces and other commercial properties. We tailor each plan to the space, the schedule and the people who use it.",
        ],
        "values_title": "How we work",
        "values": [
            ["Clear scope", "What is included, how often and at what price, all in writing before we start."],
            ["Responsive communication", "Quote requests receive a reply within 1 business day, and we keep the same line open once service begins."],
            ["Care for your space", "We treat your property and your equipment as we would want ours treated."],
            ["Bilingual service", "Our team and this website work in English and Spanish."],
        ],
        "contact_meta_title": "Contact & Free Quote | ABC Midwest Cleaning",
        "contact_meta_desc": "Request a free commercial cleaning quote from ABC Midwest. Call, email or send the form and we will reply within 1 business day.",
        "contact_h1": "Contact us",
        "contact_lead": "Tell us about your space. We reply to quote requests within 1 business day.",
        "contact_direct": "Prefer to reach us directly?",
        "f_name": "Full name", "f_email": "Email", "f_phone": "Phone", "f_company": "Company",
        "f_property": "Property type", "f_service": "Service", "f_message": "Message",
        "f_select": "Select an option", "f_required": "Required field", "f_optional": "optional",
        "f_send": "Send request", "f_sending": "Sending…",
        "f_success": "Thank you! We received your request and will reply within 1 business day.",
        "f_error": "Something went wrong. Please try again or contact us by phone or email.",
        "f_mailto": "Your email app should open with your request ready to send. If it does not, write to us directly.",
        "f_invalid": "Please complete the required fields.",
        "f_honeypot": "Leave this field empty",
        "f_privacy": "By sending this form you agree to our",
        "properties": ["Office", "Retail / storefront", "Medical or professional suite", "Warehouse / industrial", "Education / community", "Other"],
        "f_service_other": "Not sure yet",
        "privacy_link": "Privacy Policy",
        "privacy_meta_title": "Privacy Policy | ABC Midwest",
        "privacy_meta_desc": "How ABC Midwest collects, uses and protects information submitted through this website.",
        "terms_meta_title": "Terms of Use | ABC Midwest",
        "terms_meta_desc": "Terms that apply to the use of the ABC Midwest website and to quote requests submitted through it.",
        "nf_title": "Page not found",
        "nf_text": "The page you are looking for does not exist or has moved.",
        "nf_home": "Back to home", "nf_meta_title": "Page not found | ABC Midwest",
        "nf_meta_desc": "The page you requested could not be found.",
        "legal_links": "Legal", "privacy": "Privacy Policy", "terms": "Terms of Use",
        "rights": "All rights reserved.",
        "footer_blurb": "Commercial cleaning for offices, retail and facilities across the Midwest.",
        "footer_contact": "Contact", "footer_links": "Company", "footer_services": "Services",
        "wa_text": "Hello, I would like a cleaning quote.",
        "mobile_bar": "Quick actions",
        "draft_notice": "TEMPLATE: This text is a general template and must be reviewed by a licensed attorney before publication. Items highlighted in yellow must be completed.",
        "updated": "Last updated",
    },
    "es": {
        "lang_name": "Español", "lang_code": "ES", "html_lang": "es", "og_locale": "es_US",
        "home_h1": "Limpieza comercial para empresas del Medio Oeste",
        "about_img_alt": "Equipo de limpieza preparando un espacio comercial",
        "skip": "Saltar al contenido principal",
        "nav_home": "Inicio", "nav_services": "Servicios", "nav_about": "Nosotros", "nav_contact": "Contacto",
        "menu": "Menú", "close": "Cerrar", "all_services": "Todos los servicios",
        "cta_quote": "Cotizar", "cta_call": "Llamar", "cta_whatsapp": "Escríbanos por WhatsApp",
        "call_us": "Llámenos", "email_us": "Escríbanos", "learn_more": "Ver más",
        "primary_nav": "Navegación principal", "language": "Idioma", "switch_to": "English",
        "prev": "Diapositiva anterior", "next": "Diapositiva siguiente", "pause": "Pausar presentación", "play": "Reanudar presentación",
        "go_slide": "Ir a la diapositiva",
        "breadcrumb": "Ruta de navegación",
        "facts": [
            ["1 día", "Respuesta en día hábil a las solicitudes de cotización"],
            ["24/7", "Solicitudes de cotización en línea a cualquier hora"],
            ["ES / EN", "Atención en español e inglés"],
            ["Gratis", "Cotizaciones escritas y sin compromiso"],
        ],
        "services_eyebrow": "Lo que hacemos", "services_title": "Servicios de limpieza comercial",
        "services_lead": "Elija un servicio o cuéntenos qué necesita su espacio y armaremos el plan a su medida.",
        "process_eyebrow": "Cómo funciona", "process_title": "Del primer mensaje a un espacio más limpio",
        "process": [
            ["Cuéntenos sobre su espacio", "Envíe una solicitud breve con el tipo de propiedad, la ubicación y el servicio que necesita."],
            ["Revisamos los detalles", "Confirmamos el alcance con usted y, si hace falta, revisamos el sitio."],
            ["Reciba una cotización escrita", "Alcance, frecuencia y precio por escrito, dentro de 1 día hábil desde su solicitud."],
            ["Comienza el servicio", "Iniciamos según el calendario acordado y seguimos en contacto para ajustar el plan."],
        ],
        "about_eyebrow": "Nosotros", "about_title": "Un aliado de limpieza que se comunica con claridad",
        "about_text": [
            "ABC Midwest Commercial Cleaning apoya a oficinas, locales comerciales e instalaciones con planes de limpieza confiables. Mantenemos el proceso simple: usted nos cuenta qué necesita, ponemos el plan por escrito y lo cumplimos.",
            "Atendemos en español y en inglés, para que todo su equipo hable con nosotros en el idioma en que se sienta más cómodo."
        ],
        "about_cta": "Conozca más sobre nosotros",
        "areas_title": "Zonas de servicio",
        "areas_lead": "Ofrecemos limpieza comercial en los siguientes estados. Si está cerca, consúltenos.",
        "faq_eyebrow": "Preguntas", "faq_title": "Preguntas frecuentes",
        "faq_home": [
            ["¿Qué tipos de propiedades limpian?", "Trabajamos con oficinas, locales comerciales, consultorios profesionales, áreas de oficina de bodegas y otras propiedades comerciales. Si la suya es distinta, cuéntenos y le diremos si podemos ayudarle."],
            ["¿Cómo solicito una cotización?", "Use el formulario de cotización o llámenos. Confirmamos el alcance con usted y enviamos una cotización por escrito dentro de 1 día hábil."],
            ["¿Ofrecen limpieza puntual y recurrente?", "Ambas. Los planes recurrentes se definen por frecuencia y los servicios puntuales por alcance, y todo queda detallado en su cotización."],
            ["¿Hablan español?", "Sí. Nos comunicamos en español e inglés, y este sitio web está disponible en ambos idiomas."],
            ["¿Qué zonas atienden?", "Atendemos los estados del Medio Oeste indicados en nuestras zonas de servicio. Escríbanos si no está seguro de que su ubicación esté cubierta."],
        ],
        "banner_title": "¿Listo para un lugar de trabajo más limpio?",
        "banner_text": "Cuéntenos sobre su espacio y reciba una cotización escrita dentro de 1 día hábil.",
        "trust": ["Cotización escrita gratis", "Respuesta en 1 día hábil", "Español e inglés"],
        "includes_title": "Qué incluye",
        "includes_lead": "El alcance exacto se confirma en su cotización escrita. Las tareas típicas incluyen:",
        "process_service_title": "Cómo trabajamos",
        "faq_service_title": "Preguntas sobre este servicio",
        "quote_card_title": "Solicite una cotización gratis",
        "quote_card_text": "Cuéntenos sobre su espacio y le responderemos dentro de 1 día hábil.",
        "other_services": "Otros servicios",
        "services_page_title": "Nuestros servicios",
        "services_page_h1": "Servicios de limpieza comercial",
        "services_page_lead": "Limpieza confiable para los lugares donde se hacen negocios.",
        "services_meta_title": "Servicios de limpieza comercial en el Medio Oeste | ABC Midwest",
        "services_meta_desc": "Limpieza de oficinas, post-construcción, pisos, ventanas y mantenimiento diario en el Medio Oeste. Cotización escrita gratis en 1 día hábil.",
        "home_meta_title": "Limpieza comercial en el Medio Oeste | ABC Midwest",
        "home_meta_desc": "Limpieza comercial para oficinas e instalaciones en el Medio Oeste. Atención en español e inglés y cotización escrita gratis en 1 día hábil.",
        "slides": [
            ["Espacios limpios para días productivos", "Limpieza comercial para oficinas, locales e instalaciones en el Medio Oeste.", "hero-1", "Interior de oficina comercial luminoso y ordenado"],
            ["Planificado según su horario", "Definimos ventanas de servicio que trabajan con su operación, no en contra de ella.", "hero-2", "Integrante del equipo de limpieza cuidando el piso de un vestíbulo comercial"],
            ["Solicite una cotización en minutos", "Comparta algunos datos y reciba una cotización escrita dentro de 1 día hábil.", "hero-3", "Fachada moderna y limpia de un edificio con ventanales"],
        ],
        "about_meta_title": "Nosotros | ABC Midwest, empresa de limpieza comercial",
        "about_meta_desc": "Conozca cómo trabaja ABC Midwest: comunicación clara, planes por escrito y atención en español e inglés.",
        "about_h1": "Sobre ABC Midwest",
        "about_lead": "Limpieza comercial basada en planes claros y comunicación clara.",
        "about_body": [
            "Partimos de una idea simple: un servicio de limpieza debe ser fácil de contactar y cumplir su palabra. Por eso cada contratación empieza con un alcance escrito que ambas partes entienden.",
            "Nuestro trabajo abarca oficinas, locales comerciales y otras propiedades comerciales. Adaptamos cada plan al espacio, al horario y a las personas que lo usan.",
        ],
        "values_title": "Cómo trabajamos",
        "values": [
            ["Alcance claro", "Qué incluye, con qué frecuencia y a qué precio, todo por escrito antes de empezar."],
            ["Comunicación ágil", "Las solicitudes de cotización se responden en 1 día hábil, y mantenemos la misma línea abierta cuando el servicio comienza."],
            ["Cuidado de su espacio", "Tratamos su propiedad y sus equipos como nos gustaría que trataran los nuestros."],
            ["Atención bilingüe", "Nuestro equipo y este sitio trabajan en español e inglés."],
        ],
        "contact_meta_title": "Contacto y cotización gratis | ABC Midwest Limpieza",
        "contact_meta_desc": "Solicite una cotización gratis de limpieza comercial con ABC Midwest. Llame, escriba o use el formulario y respondemos en 1 día hábil.",
        "contact_h1": "Contáctenos",
        "contact_lead": "Cuéntenos sobre su espacio. Respondemos las solicitudes de cotización dentro de 1 día hábil.",
        "contact_direct": "¿Prefiere contactarnos directamente?",
        "f_name": "Nombre completo", "f_email": "Correo electrónico", "f_phone": "Teléfono", "f_company": "Empresa",
        "f_property": "Tipo de propiedad", "f_service": "Servicio", "f_message": "Mensaje",
        "f_select": "Seleccione una opción", "f_required": "Campo obligatorio", "f_optional": "opcional",
        "f_send": "Enviar solicitud", "f_sending": "Enviando…",
        "f_success": "¡Gracias! Recibimos su solicitud y le responderemos dentro de 1 día hábil.",
        "f_error": "Algo salió mal. Inténtelo de nuevo o contáctenos por teléfono o correo.",
        "f_mailto": "Se abrirá su aplicación de correo con la solicitud lista para enviar. Si no se abre, escríbanos directamente.",
        "f_invalid": "Complete los campos obligatorios.",
        "f_honeypot": "Deje este campo vacío",
        "f_privacy": "Al enviar este formulario acepta nuestra",
        "properties": ["Oficina", "Local comercial", "Consultorio o suite profesional", "Bodega / industrial", "Educación / comunidad", "Otro"],
        "f_service_other": "Aún no estoy seguro",
        "privacy_link": "Política de privacidad",
        "privacy_meta_title": "Política de privacidad | ABC Midwest",
        "privacy_meta_desc": "Cómo ABC Midwest recopila, usa y protege la información enviada a través de este sitio web.",
        "terms_meta_title": "Términos de uso | ABC Midwest",
        "terms_meta_desc": "Términos que se aplican al uso del sitio web de ABC Midwest y a las solicitudes de cotización enviadas por este medio.",
        "nf_title": "Página no encontrada",
        "nf_text": "La página que busca no existe o fue movida.",
        "nf_home": "Volver al inicio", "nf_meta_title": "Página no encontrada | ABC Midwest",
        "nf_meta_desc": "No se encontró la página solicitada.",
        "legal_links": "Legal", "privacy": "Política de privacidad", "terms": "Términos de uso",
        "rights": "Todos los derechos reservados.",
        "footer_blurb": "Limpieza comercial para oficinas, locales e instalaciones en el Medio Oeste.",
        "footer_contact": "Contacto", "footer_links": "Empresa", "footer_services": "Servicios",
        "wa_text": "Hola, quisiera una cotización de limpieza.",
        "mobile_bar": "Acciones rápidas",
        "draft_notice": "PLANTILLA: Este texto es una plantilla general y debe ser revisado por un abogado con licencia antes de publicarse. Los puntos resaltados en amarillo deben completarse.",
        "updated": "Última actualización",
    },
}

# ------------------------------------------------------------ páginas legales
# Marcadores {{...}} se convierten en <mark class="todo"> en la página.
LEGAL = {
    "privacy": {
        "en": {
            "h1": "Privacy Policy",
            "sections": [
                ["Who we are", ["This website is operated by {{LEGAL ENTITY NAME}} (\"ABC Midwest\", \"we\", \"us\"). You can contact us at {{EMAIL}} or {{MAILING ADDRESS}}."]],
                ["Information we collect", ["When you submit the contact or quote form we collect the details you provide: name, email, phone number, company, property type, selected service and your message.", "Our hosting provider may automatically record technical data such as IP address, browser type and pages visited, for security and basic operation of the site. {{Confirm any analytics, cookies or advertising tools you use, and describe them here.}}"]],
                ["How we use information", ["We use the information to respond to quote requests, provide and improve our services, communicate with you and protect the site against abuse.", "We do not sell your personal information."]],
                ["Sharing", ["We may share information with service providers that help us operate the website and the business (for example hosting and form-processing services: {{LIST PROVIDERS}}), and when required by law."]],
                ["Retention and security", ["We keep information only as long as needed for the purposes above or as required by law. We use reasonable measures to protect information, but no method of transmission over the internet is completely secure. {{Define retention period.}}"]],
                ["Your choices and rights", ["You may ask us to access, correct or delete your information by contacting us. {{Add rights required by the laws that apply to you (for example state privacy laws).}}"]],
                ["Children", ["This website is intended for businesses and is not directed to children under 13."]],
                ["Changes", ["We may update this policy and will post the new version on this page with a new date."]],
            ]
        },
        "es": {
            "h1": "Política de privacidad",
            "sections": [
                ["Quiénes somos", ["Este sitio web es operado por {{NOMBRE LEGAL DE LA EMPRESA}} (\"ABC Midwest\", \"nosotros\"). Puede contactarnos en {{CORREO}} o {{DIRECCIÓN POSTAL}}."]],
                ["Información que recopilamos", ["Cuando envía el formulario de contacto o cotización recopilamos los datos que usted proporciona: nombre, correo, teléfono, empresa, tipo de propiedad, servicio seleccionado y su mensaje.", "Nuestro proveedor de hosting puede registrar automáticamente datos técnicos como la dirección IP, el tipo de navegador y las páginas visitadas, por seguridad y para el funcionamiento básico del sitio. {{Confirme qué herramientas de analítica, cookies o publicidad utiliza y descríbalas aquí.}}"]],
                ["Cómo usamos la información", ["Usamos la información para responder solicitudes de cotización, prestar y mejorar nuestros servicios, comunicarnos con usted y proteger el sitio contra abusos.", "No vendemos su información personal."]],
                ["Con quién la compartimos", ["Podemos compartir información con proveedores que nos ayudan a operar el sitio y el negocio (por ejemplo servicios de hosting y de procesamiento de formularios: {{LISTA DE PROVEEDORES}}), y cuando la ley lo exija."]],
                ["Conservación y seguridad", ["Conservamos la información solo el tiempo necesario para los fines anteriores o el que exija la ley. Usamos medidas razonables para protegerla, pero ningún método de transmisión por internet es totalmente seguro. {{Defina el plazo de conservación.}}"]],
                ["Sus opciones y derechos", ["Puede solicitarnos acceso, corrección o eliminación de su información escribiéndonos. {{Agregue los derechos exigidos por las leyes que le apliquen (por ejemplo, leyes estatales de privacidad).}}"]],
                ["Menores de edad", ["Este sitio está dirigido a empresas y no a menores de 13 años."]],
                ["Cambios", ["Podemos actualizar esta política y publicaremos la nueva versión en esta página con una nueva fecha."]],
            ]
        },
    },
    "terms": {
        "en": {
            "h1": "Terms of Use",
            "sections": [
                ["Acceptance", ["By using this website you agree to these terms. If you do not agree, please do not use the site. The site is operated by {{LEGAL ENTITY NAME}}."]],
                ["Information on this site", ["The content is provided for general information. Descriptions of services are not an offer or contract. The scope, schedule and price of any service are defined only in a written quote or agreement signed or accepted by both parties."]],
                ["Quote requests", ["Submitting a form does not create a service agreement. Quotes are estimates based on the information you provide and may change if the conditions of the property differ."]],
                ["Acceptable use", ["You agree not to misuse the site, attempt to disrupt it, send unlawful or misleading content, or use automated means to submit forms."]],
                ["Intellectual property", ["The text, design and other materials on this site belong to {{LEGAL ENTITY NAME}} or its licensors and may not be copied or reused without permission."]],
                ["Disclaimer and liability", ["The site is provided \"as is\". To the extent permitted by law, we are not liable for indirect or consequential damages arising from the use of the site. {{Have an attorney define warranty and liability language.}}"]],
                ["Governing law", ["These terms are governed by the laws of {{STATE / GOVERNING LAW}}, and disputes will be handled in {{VENUE / COURTS}}."]],
                ["Changes and contact", ["We may update these terms at any time by posting a new version. Questions: {{EMAIL}}."]],
            ]
        },
        "es": {
            "h1": "Términos de uso",
            "sections": [
                ["Aceptación", ["Al usar este sitio web usted acepta estos términos. Si no está de acuerdo, no utilice el sitio. El sitio es operado por {{NOMBRE LEGAL DE LA EMPRESA}}."]],
                ["Información de este sitio", ["El contenido se ofrece con fines informativos generales. Las descripciones de los servicios no constituyen una oferta ni un contrato. El alcance, el calendario y el precio de cualquier servicio se definen únicamente en una cotización o acuerdo escrito firmado o aceptado por ambas partes."]],
                ["Solicitudes de cotización", ["Enviar un formulario no crea un acuerdo de servicio. Las cotizaciones son estimaciones basadas en la información que usted proporciona y pueden cambiar si las condiciones de la propiedad son distintas."]],
                ["Uso aceptable", ["Usted se compromete a no hacer un uso indebido del sitio, no intentar interrumpirlo, no enviar contenido ilícito o engañoso y no usar medios automatizados para enviar formularios."]],
                ["Propiedad intelectual", ["Los textos, el diseño y demás materiales de este sitio pertenecen a {{NOMBRE LEGAL DE LA EMPRESA}} o a sus licenciantes y no pueden copiarse ni reutilizarse sin permiso."]],
                ["Exclusión de garantías y responsabilidad", ["El sitio se ofrece \"tal cual\". En la medida permitida por la ley, no somos responsables de daños indirectos o consecuentes derivados del uso del sitio. {{Pida a un abogado definir el texto de garantías y responsabilidad.}}"]],
                ["Ley aplicable", ["Estos términos se rigen por las leyes de {{ESTADO / LEY APLICABLE}}, y las controversias se resolverán en {{JURISDICCIÓN / TRIBUNALES}}."]],
                ["Cambios y contacto", ["Podemos actualizar estos términos en cualquier momento publicando una nueva versión. Preguntas: {{CORREO}}."]],
            ]
        },
    },
}
