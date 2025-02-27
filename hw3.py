from typing import List
from build_data import CountyDemographics

#task 1
#parameter type list and outputs an integer of combined populations in counties
#code sums the population
def population_total(counties: list[CountyDemographics]) -> int:
    return sum(county.population.get('2014 Population', 0) for county in counties)


#task 2
#parameter type is list from CountryDemographics and a specific state abbreviated and outputs a list of data from the specific state
#code only returns info when state abbreviation is called
def filter_by_state(counties: list[CountyDemographics], abbr: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == abbr]

#Task 3
#part 1
#parameter type county lists and specific education_key interests and returns total population of the countries as a float
#code starts total_population at 0 and adds the education population by multiplying population by demographic
def population_by_education(counties, education_key):
    total_population = 0
    for county in counties:
        if education_key in county.education:
            total_population += (county.education[education_key] / 100) * county.population['2014 Population']
    return total_population

#part 2
def population_by_ethnicity(counties, ethnicity_key):
    total_population = 0
    for county in counties:
        if ethnicity_key in county.ethnicities:
            total_population += (county.ethnicities[ethnicity_key] / 100) * county.population['2014 Population']
    return total_population

#part 3
def population_below_poverty_level(counties):
    total_population = 0
    for county in counties:
        if 'Persons Below Poverty Level' in county.income:
            total_population += (county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population']
    return total_population

#Task 4
#part 1
#parameter of list of county demographic and specific education_key, ethnicity_key, poverty level interests and returns subpop across provided counties
#code finds ratio of total population in counties and population of key interest and turns into a percentage by multiplying 100
def percent_by_education(counties: List[CountyDemographics], education_key: str) -> float:
    total_population = population_total(counties)
    education_population = population_by_education(counties, education_key)
    if total_population == 0:
        return 0
    return (education_population / total_population) * 100

#part 2
def percent_by_ethnicity(counties: List[CountyDemographics], ethnicity_key: str) -> float:
    total_population = population_total(counties)
    ethnicity_population = population_by_ethnicity(counties, ethnicity_key)
    if total_population == 0:
        return 0
    return (ethnicity_population / total_population) * 100

#part 3
def percent_below_poverty_level(counties: List[CountyDemographics]) -> float:
    total_population = population_total(counties)
    poverty_population = population_below_poverty_level(counties)
    if total_population == 0:
        return 0
    return (poverty_population / total_population) * 100

#Task 5
#takes parameters lists of counties, specific interest keys, and a threshold float value (beginning) and returns if satisfies the boolean requirments
#codes take the special interest and run it through a true or false boolean wheather its grater than or equal to the threashold value being 0
#part 1
def education_greater_than(counties: List[CountyDemographics], education_key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) > threshold]

def education_less_than(counties: List[CountyDemographics], education_key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) < threshold]

#part 2
def ethnicity_greater_than(counties: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) > threshold]

def ethnicity_less_than(counties: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) < threshold]

#part 3
def below_poverty_level_greater_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) > threshold]

def below_poverty_level_less_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) < threshold]
