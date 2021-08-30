DROP VIEW "main"."henkilon_viimeiset_tiedot";
CREATE VIEW henkilon_viimeiset_tiedot AS
SELECT henkilon_viimeisin_mittaus.henkilo_id, etunimi, sukunimi, sukupuoli, pituus, paino, ika
FROM henkilon_viimeisin_mittaus INNER JOIN henkilo_mittaus_ika_v2 ON henkilon_viimeisin_mittaus.viimeisin_mittaus_id = henkilo_mittaus_ika_v2.mittaus_id