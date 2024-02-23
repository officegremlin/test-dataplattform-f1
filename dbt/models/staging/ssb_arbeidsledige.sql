select 
    type_justering
    ,substring(maaned,1,4)::int as aar
    ,substring(maaned,6,2)::int as maaned
    ,verdi as verdi_prosent
    
from {{ source('ssb', 'SSB_ARBEIDSLEDIGE_13MND') }}