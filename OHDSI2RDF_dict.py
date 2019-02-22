#! /usr/bin/env python

### Read from Athena CPT processed Vocabulary files and Ananke UMLS CUI mappings into RDF turtle graph
### Created by: Juan M. Banda - Panacea Lab - Georgia State University
### Version 0.5
### Created during Biomedical Linked Annotation Hackathon (BLAH5) in Kashiwa, Japan
### http://blah5.linkedannotation.org/
###
import csv

HEADER = """
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix umls: <http://bioportal.bioontology.org/ontologies/umls/> .
"""

print (HEADER)

with open("VOCABULARY.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar="'")
    next(rd)
    for row in rd:
        if row[0]=='None':
                        print("<http://www.ohdsi.org/OHDSIVocab/OHDSIVocabulary>")
                        print("    a owl:Ontology ;")
                        print('    rdfs:comment "' + row[1] + '" ;')
                        print('    rdfs:label "' + row[2] + '" ;')
                        print("    owl:imports <http://www.w3.org/2004/02/skos/core> ;")
                        print('    owl:versionInfo "' + row[3] + '"')
                        print(".")

## Get the Vocabulary relations ##
with open("VOCABULARY.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar="'")
    next(rd)
    for row in rd:
	if row[0]!='None':
			print('<http://www.ohdsi.org/OHDSIVocab/Vocabulary/' + (row[0].replace(' ','_')).replace('/','_') + '> a owl:Class ;')
			print('        skos:prefLabel """' + row[1] + '"""@en ;')
			print('        skos:concept """' + row[0] + '"""^^xsd:string ;')
			print('        <http://www.ohdsi.org/OHDSIVocab/vocabulary_name> """' + row[1] + '"""^^xsd:string ;')
			print('        <http://www.ohdsi.org/OHDSIVocab/vocabulary_reference> """' + row[2] + '"""^^xsd:string ;')
			print('        <http://www.ohdsi.org/OHDSIVocab/vocabulary_version> """' + row[3] + '"""^^xsd:string ;')
			print('        <http://www.ohdsi.org/OHDSIVocab/vocabulary_concept_id> """' + row[4] + '"""^^xsd:string ;')
			print(".")

## Get the domain relations ##
with open("DOMAIN.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar="'")
    next(rd)
    for row in rd:
		print('<http://www.ohdsi.org/OHDSIVocab/Domain/' + (row[0].replace(' ','_')).replace('/','_') + '> a owl:Class ;')
		print('        skos:prefLabel """' + row[1] + '"""@en ;')
		print('        skos:concept """' + row[2] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/domain_id> """' + row[0].replace(' ','_') + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/domain_name> """' + row[1] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/domain_concept_id> """' + row[2] + '"""^^xsd:string ;')
		print('.')

## Get the concept_class relations ##
with open("CONCEPT_CLASS.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar="'")
    next(rd)
    for row in rd:
		print('<http://www.ohdsi.org/OHDSIVocab/Concept_class/' + (row[0].replace(' ','_')).replace('/','_') + '> a owl:Class ;')
		print('        skos:prefLabel """' + row[1] + '"""@en ;')
		print('        skos:concept """' + row[2] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_class_id> """' + (row[0].replace(' ','_')).replace('/','_') + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_class_name> """' + row[1] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_class_concept_id> """' + row[2] + '"""^^xsd:string ;')
		print('.')

### We want to read the Annanke Mappings in memory for faster searches of the corresponding CUI
an_dict = {}
with open("AnankeV2.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar="\"")
    next(reader)
    for row_D in reader:
	an_dict.update( {row_D[1] : row_D[0]} )

## Now for the main concept mappings ##
with open("CONCEPT.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar="'")
    next(rd) ## Remove pesky header
    for row in rd:
		print('<http://athena.ohdsi.org/search-terms/terms/' + row[0] + '> a owl:Class ;')
		print('        skos:prefLabel """' + row[1].replace('"','\\"') + '"""@en ;')
		print('        skos:concept """' + row[0] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_id> """' + row[0] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_name> """' + row[1].replace('"','\\"') + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/domain_id> <http://www.ohdsi.org/OHDSIVocab/Domain/'+ (row[2].replace(' ','_')).replace('/','_') +'> ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/vocabulary_id> <http://www.ohdsi.org/OHDSIVocab/Vocabulary/'+ (row[3].replace(' ','_')).replace('/','_') +'> ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_class_id> <http://www.ohdsi.org/OHDSIVocab/Concept_class/'+ (row[4].replace(' ','_')).replace('/','_') +'> ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/standard_concept> """' + row[5] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/concept_code> """' + row[6] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/valid_start_date> """' + row[7] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/valid_end_date> """' + row[8] + '"""^^xsd:string ;')
		print('        <http://www.ohdsi.org/OHDSIVocab/invalid_reason> """' + row[9] + '"""^^xsd:string ;')
		### This snippet finds the appropiate UMLS CUI mapping if available
		mappingC=an_dict.get(row[0], 'NA')
		if mappingC != 'NA':
			print('        umls:cui """' + mappingC + ' """^^xsd:string ;') 
		### This could be a looooot more efficient.... but works for now
		#for iR in range(0,len(data)-1):
		#	if data[iR]['concept_id']==row[0]:
		#		print('        umls:cui """' + data[iR]['CUI'] + ' """^^xsd:string ;')
		#		break
		print(' .')

##Footer of the document ###
print('''
<http://www.ohdsi.org/OHDSIVocab/concept_id> a owl:ObjectProperty ;
        rdfs:label """Concept ID""";
        rdfs:comment """OHDSI Concept ID""" .
 <http://www.ohdsi.org/OHDSIVocab/concept_name> a owl:ObjectProperty ;
        rdfs:label """Concept Name""";
        rdfs:comment """OHDSI Concept Name""" .
 <http://www.ohdsi.org/OHDSIVocab/domain_id> a owl:ObjectProperty ;
        rdfs:label """Domain ID""";
        rdfs:comment """OHDSI Concept Domain ID""" .
 <http://www.ohdsi.org/OHDSIVocab/domain_name> a owl:ObjectProperty ;
        rdfs:label """Domain Name""";
        rdfs:comment """OHDSI Domain Name""" .
 <http://www.ohdsi.org/OHDSIVocab/domain_concept_id> a owl:ObjectProperty ;
        rdfs:label """Domain Concept ID""";
        rdfs:comment """OHDSI Domain Concept ID""" .
 <http://www.ohdsi.org/OHDSIVocab/vocabulary_id> a owl:ObjectProperty ;
        rdfs:label """Vocabulary ID""";
        rdfs:comment """OHDSI Concept Vocabulary ID""" .
 <http://www.ohdsi.org/OHDSIVocab/vocabulary_name> a owl:ObjectProperty ;
        rdfs:label """Vocabulary Name""";
        rdfs:comment """OHDSI Vocabulary Name""" .
 <http://www.ohdsi.org/OHDSIVocab/vocabulary_reference> a owl:ObjectProperty ;
        rdfs:label """Vocabulary Reference""";
        rdfs:comment """OHDSI Vocabulary Reference""" .
 <http://www.ohdsi.org/OHDSIVocab/vocabulary_version> a owl:ObjectProperty ;
        rdfs:label """Vocabulary Version""";
        rdfs:comment """OHDSI Vocabulary Version""" .
 <http://www.ohdsi.org/OHDSIVocab/vocabulary_concept_id> a owl:ObjectProperty ;
        rdfs:label """Vocabulary Concept ID""";
        rdfs:comment """OHDSI Vocabulary Concept ID""" .
 <http://www.ohdsi.org/OHDSIVocab/concept_class_id> a owl:ObjectProperty ;
        rdfs:label """Concept Class ID""";
        rdfs:comment """OHDSI Concept Class ID""" .
 <http://www.ohdsi.org/OHDSIVocab/concept_class_name> a owl:ObjectProperty ;
        rdfs:label """Concept Class Name""";
        rdfs:comment """OHDSI Concept Class Name""" .
 <http://www.ohdsi.org/OHDSIVocab/concept_class_concept_id> a owl:ObjectProperty ;
        rdfs:label """Concept Class Concept ID""";
        rdfs:comment """OHDSI Concept Class Concept ID""" .
 <http://www.ohdsi.org/OHDSIVocab/standard_concept> a owl:ObjectProperty ;
        rdfs:label """Standard Concept""";
        rdfs:comment """OHDSI Standard Concept""" .
 <http://www.ohdsi.org/OHDSIVocab/concept_code> a owl:ObjectProperty ;
        rdfs:label """Concept Code""";
        rdfs:comment """Source Vocabulary Concept Code""" .
 <http://www.ohdsi.org/OHDSIVocab/valid_start_date> a owl:ObjectProperty ;
        rdfs:label """Valid Start Date""";
        rdfs:comment """OHDSI Concept Valid Start Date""" .
 <http://www.ohdsi.org/OHDSIVocab/valid_end_date> a owl:ObjectProperty ;
        rdfs:label """Valid End Date""";
        rdfs:comment """OHDSI Concept Valid End Date""" .
 <http://www.ohdsi.org/OHDSIVocab/invalid_reason> a owl:ObjectProperty ;
        rdfs:label """Invalid Reason""";
        rdfs:comment """OHDSI Concept Invalid Reason""" .
''')
