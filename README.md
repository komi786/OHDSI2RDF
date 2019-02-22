# OHDSI2RDF

### Fully connecting the Observational Health Data Science and Informatics (OHDSI) initiative with the world of linked open data

![sample](http://www.jmbanda.com/sample_tripple.png)

Leveraging [Ananke](https://github.com/thepanacealab/OHDSIananke), the utility here converts [Athena](http://athena.ohdsi.org/) vocbulary files into one large Turtle file containing the vocabulary converted to an RDF graph.

This work was conceptualized for/and (mostly) carried out while at the [Biomedical Linked Annotation Hackathon 5](http://blah5.linkedannotation.org/) in Kashiwa, Japan.

![BLAH](http://www.jmbanda.com/customLogo.gif)

We are veru grateful for the support on this work.

## Usage Instructions:

There are three versions of this utility: OHDSI2RDF_dict.py, OHDSI2RDF.py and OHDSI2RDF_mp.py. The first one uses a dictionary, the second one is single threaded and the third program uses multi-processing. However, the second one seems slower, so be sure to try them.

Assumptions: This program assumes that you have the OHDSI vocabulary CSV files extracted in the folder you are running this code and they have the standard uppercase named files. The second assumption is that you have the Ananke mappings in the standard CSV file provided. 

How to run
```
python OHDSI2RDF_dict.py >> OHDSI2RDF.ttl 
```

The program outputs to the screen, so be sure to capture the output on a file. 

#### NOTE: With enough RAM this runs in about 15 minutes

## Release Notes: 

### Version 1.0:  Relationships included: Vocabulary, Domain, Concept_class, Concept

## TO DO
* Add ancestor and Synonym relationships
* Improve CUI assigning from Ananke source 

![OHDSIlogo](http://www.jmbanda.com/t-ohdsi-logo-only.png)
![RDFtripple](http://www.jmbanda.com/rdf.png)


