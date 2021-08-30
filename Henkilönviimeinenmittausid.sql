DROP VIEW "main"."henkilon_viimeisin_mittaus";
CREATE VIEW henkilon_viimeisin_mittaus AS
SELECT henkilo_id, max(mittaus_id) AS viimeisin_mittaus_id
FROM henkilo_mittaus_ika_v2
GROUP BY henkilo_id