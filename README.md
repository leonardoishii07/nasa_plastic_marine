# Summary

Marine debris is one of the most pervasive threats to the health of coastal areas, oceans, and waterways. Your challenge is to leverage Artificial Intelligence/Machine Learning to monitor, detect, and quantify plastic pollution and increase our understanding about using these techniques for this purpose.

# Details
## BACKGROUND

Marine debris is one of the most pervasive threats to the health of coastal areas, oceans, and waterways. It is an issue of local, regional, national, and international concern. Marine debris can injure or kill marine fauna, damage and degrade habitats, interfere with navigational safety, cause economic loss to fishing and maritime industries, degrade the quality of life in coastal communities, and threaten human health and safety. It is believed that at least eight million tons of plastic end up in our oceans every year and comprise 80% of all marine debris present—from surface waters down to deep-sea sediments.

The U.S. Marine Debris Research, Prevention, and Reduction Act defines marine debris as "any persistent solid material that is manufactured or processed and directly or indirectly, intentionally or unintentionally, disposed of or abandoned into the Marine environment or connecting systems" (https://www.epa.gov/trash-free-waters/toxicological-threats-plastic). Marine debris of varying size—from microscopic particles to objects that are several meters long—is ubiquitous in the global ocean. However, it is difficult to track and quantify how much marine debris is currently in the ocean and determine where the highest concentrations are, how it is distributed, and how debris is interacting with the biological elements in the ocean. This information is critical to formulate and enact any type of mitigation strategy to address the marine debris problem.

While marine debris enters the ocean daily through atmospheric deposition (wind-blown trash), river discharge, and improper disposal of fishing and vessel waste, major debris events caused by disasters also contribute significantly. For example, hurricanes and landslides can carry large amounts of debris—ranging from toppled housing and infrastructure to small pieces of trash—into the ocean. Tracking where this debris is and what happens to it is fundamental to ensure a sustainable and healthy ocean.

The marine debris problem has been widely recognized; there are several initiatives, nationally and internationally, dedicated to devising strategies to address the debris issue.

## OBJECTIVES

Your challenge is to leverage geospatial technology and apply Artificial Intelligence/Machine Learning (AI/ML) capabilities to monitor, detect, and quantify plastic marine debris. Specifically, are there potential advantages as well as the limitations of utilizing AI/ML algorithms to quickly and inexpensively classify plastic pollution and report/visualize the findings in a publicly accessible way?

Currently, marine debris observation systems are in their infancy. Due to the broad diversity of sizes, types, shapes, buoyancy, and chemical composition of the debris, remote sensing is the only technology capable of providing the uniform observation necessary to address this challenge. Your solution should input remote sensing data into a database that can be built into a dashboard to enable access to this information.

To address this challenge, you will use existing remote sensing data on plastics and apply AI/ML capabilities to:

1) Create a visualization database based on AI/ML algorithms that will aid in classifying and detecting these plastics using remote sensing data. Look to sites like The Global Forest Watch, funded in part by USAID, for examples.

2) Understand the potential advantages and limitations of utilizing AI/ML algorithms to classify plastic pollution.

Your solution should allow data on plastic waste to be more accessible and valuable to citizen scientists, remote-sensing experts, as well as policy makers and regulators. It should enable scientists to better detect plastics utilizing remote sensing data and policy makers to use this information to effectuate change.

## POTENTIAL CONSIDERATIONS

When developing your solution, you may (but are not required to) consider the following:

Please consider utilizing citizen science data from apps. Search the app store for “Debris Tracker.”
When classifying the data, please include a timestamp, location, depth, and note whether it is a single item of debris, patch, or filament.
Potential keywords you may search: global forest watch, ocean scan, debris tracker
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

NASA does not endorse any non-U.S. Government entity and is not responsible for information contained on non-U.S. Government websites.

## [Aproveitando AI / ML para detritos marinhos de plástico](!https://spaceterra.org/desafios-2021/)

Os detritos marinhos são uma das ameaças mais comuns à saúde das áreas costeiras, oceanos e hidrovias. Seu desafio é aproveitar a Inteligência Artificial / Aprendizado de Máquina para monitorar, detectar e quantificar a poluição de plástico e aumentar nossa compreensão sobre o uso dessas técnicas para essa finalidade.

# Run Docker File
## Install package
`$ pip install -r requirements `

## Run
`$ python app.py `