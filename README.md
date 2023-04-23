# Bus_Rider
Study project

easyride:
Checks buses data given in the JSON format and verifies compliance with requirement.
    Example:
    [
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
    Requiriments for data format and data filling
    
    "bus_id"      - integer - must be filled
    "stop_id"     - integer - must be filled
    "stop_name"   - string  - must be filled
              requiered format: [proper name][suffix]
                                Suffix: Road|Avenue|Boulevard|Street
                                Proper name starts with the capital latter
    "next_stop"   - integer - must be filled
    "stop_type"   - character - may not be filled
              requiered format: S (for starting stop)
                                O (for stop on demand)
                                F (for final stop)
    "a_time"      - string - must be filled
              requiered format: HH:MM (24-hour date format)
              
  
  Script print quantity of data type errors and wrong fill of the fields.
