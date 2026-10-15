SELECT DISTINCT
    common_name,
    location_name
FROM public.phillybirds
WHERE observation_datetime::date = CURRENT_DATE - INTERVAL '1 day'
ORDER BY common_name, location_name;
