FUNDING_ROUNDS = (
    ('bootstrapping', 'Bootstrapping stage'),
    ('pre_seed', 'Pre-seed stage'),
    ('seed', 'Seed stage'),
    ('growth', 'Growth stage'),
    ('series_a', 'Growth stage - Series A'),
    ('series_b', 'Growth stage - Series B'),
    ('series_c', 'Growth stage - Series C and C+'),
)

LAUNCH_STATUS_CHOICES = (
        ('public', 'Yes, it’s public'),
        ('public_beta', 'Yes, it’s in public Beta'),
        ('private_beta', 'Yes, it’s in private Beta'),
        ('no', 'No'),
    )

INDUSTRY_CHOICES = (
        ('fintech', 'Fintech'),
        ('health', 'Health'),
        ('smart_cities', 'Smart Cities'),
        ('biotech', 'Biotech'),
        ('collaboration', 'Collaboration'),
        ('entertainment', 'Entertainment'),
        ('it_tools', 'IT Tools'),
        ('security', 'Security'),
        ('sports', 'Sports'),
        ('real_estate', 'Real Estate'),
        ('transportation', 'Transportation'),
        ('media', 'Media'),
        ('hr', 'HR'),
        ('education', 'Education'),
        ('marketing', 'Marketing'),
        ('customer_success', 'Customer Success'),
        ('retail', 'Retail'),
        ('ecommerce', 'eCommerce'),
        ('industrial', 'Industrial'),
        ('software', 'Software (Sector-Agnostic)'),
    )

VERTICAL_CHOICES = (
    ('adtech_media_tech', 'Adtech / Media tech'),
    ('advanced_manufacturing', 'Advanced manufacturing'),
    ('agtech_farmtech', 'Agtech / Farmtech'),
    ('ai_ml', 'Artificial intelligence and machine learning (AI/ML)'),
    ('audiotech', 'Audiotech'),
    ('augmented_reality', 'Augmented reality (AR)'),
    ('autonomous_cars', 'Autonomous cars'),
    ('b2b_payments', 'B2B payments'),
    ('beauty', 'Beauty'),
    ('big_data', 'Big Data'),
    ('biotech', 'Biotech'),
    ('cannabis', 'Cannabis'),
    ('carsharing', 'Carsharing'),
    ('cleantech', 'Cleantech'),
    ('climate_tech', 'Climate tech'),
    ('cloudtech_devops', 'Cloudtech and DevOps'),
    ('construction_technology', 'Construction technology'),
    ('cryptocurrency_blockchain', 'Cryptocurrency and blockchain'),
    ('cybersecurity', 'Cybersecurity'),
    ('deeptech', 'Deeptech'),
    ('digital_health', 'Digital health'),
    ('ecommerce', 'Ecommerce'),
    ('edtech', 'Edtech'),
    ('ephemeral_content', 'Ephemeral content'),
    ('esports_sport_tech', 'eSports / Sport tech'),
    ('fashiontech', 'Fashiontech'),
    ('femtech', 'Femtech'),
    ('fintech', 'Fintech'),
    ('foodtech', 'Foodtech'),
    ('gaming', 'Gaming'),
    ('healthtech', 'Healthtech'),
    ('hrtech', 'HRtech'),
    ('impact_investing', 'Impact investing'),
    ('industrials', 'Industrials'),
    ('infrastructure', 'Infrastructure'),
    ('insurtech', 'Insurtech'),
    ('iot', 'Internet of Things (IoT)'),
    ('legal_tech', 'Legal tech'),
    ('life_sciences', 'Life sciences'),
    ('lohas_wellness', 'Lifestyles of Health and Sustainability (LOHAS) and wellness'),
    ('logitech_logistics', 'Logitech / Logistics'),
    ('manufacturing', 'Manufacturing'),
    ('marketing_tech', 'Marketing tech'),
    ('micro_mobility', 'Micro-mobility'),
    ('mobile', 'Mobile'),
    ('mobile_commerce', 'Mobile commerce'),
    ('mobility_tech', 'Mobility tech'),
    ('mortgage_tech', 'Mortgage tech'),
    ('nanotechnology', 'Nanotechnology'),
    ('oil_gas', 'Oil and gas'),
    ('oncology', 'Oncology'),
    ('pet_tech', 'Pet tech'),
    ('proptech', 'Real estate tech / Proptech'),
    ('restaurant_tech', 'Restaurant tech'),
    ('ridesharing', 'Ridesharing'),
    ('robotics_drones', 'Robotics and drones'),
    ('saas', 'Software as a service (SaaS)'),
    ('space_tech', 'Space tech'),
    ('supply_chain', 'Supply chain technology'),
    ('sustainability', 'Sustainability'),
    ('traveltech', 'Traveltech'),
    ('tmt', 'Technology, media and telecommunications (TMT)'),
    ('virtual_reality', 'Virtual reality (VR)'),
    ('wearables_quantified_self', 'Wearables and quantified self'),
    ('3d_printing', '3D printing'),
)

INVESTOR_TYPES = (
    ('accelerator', 'Accelerator'),
    ('angel', 'Angel investor'),
    ('corporate', 'Corporate investor'),
    ('family_office', 'Family office'),
    ('foundation', 'Foundation'),
    ('government', 'Government investor'),
    ('hedge_fund', 'Hedge fund'),
    ('incubator', 'Incubator'),
    ('pe', 'Private equity firm'),
    ('pension_fund', 'Pension fund'),
    ('sovereign_wealth_fund', 'Sovereign wealth fund'),
    ('vc', 'Venture capitalist')
)

REGION_CHOICES = (
    ('mena', 'MENA (Middle East and North Africa)'),
    ('africa', 'Africa'),
    ('south_asia', 'South Asia (India, Pakistan, Sri Lanka, Bangladesh)'),
)

TARGET_CUSTOMER_LOCATIONS = [
    ('africa', 'Africa (excluding North Africa)'),
    ('australia_new_zealand', 'Australia and New Zealand'),
    ('east_asia', 'East Asia'),
    ('europe', 'Europe'),
    ('latin_america', 'Latin America'),
    ('mena', 'MENA (Middle East and North Africa)'),
    ('north_america', 'North America (Canada, USA, Mexico)'),
    ('south_asia', 'South Asia'),
    ('south_east_asia', 'South East Asia'),
]

SALES_TYPE_CHOICES = (
    ('B2B', 'B2B'),
    ('B2C', 'B2C'),
    ('B2G', 'B2G'),
    ('C2C', 'C2C'),
    ('B2B2C', 'B2B2C'),
    ('other', 'Other/Not sure'),)

AGE_CHOICES = (
        (18, '18-24'),
        (25, '25-34'),
        (35, '35-44'),
        (45, '45-54'),
        (55, '55+'),
    )

EDUCATION_CHOICES = (
        ('high_school', 'High School'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('other', 'Other'),
    )