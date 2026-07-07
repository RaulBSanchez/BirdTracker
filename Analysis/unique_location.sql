
SELECT 
    common_name,
    MIN(location_name) AS only_seen_at
FROM public.phillybirds
WHERE observation_datetime::date = CURRENT_DATE - INTERVAL '1 day'
GROUP BY common_name
HAVING COUNT(DISTINCT location_name) = 1
ORDER BY common_name;

