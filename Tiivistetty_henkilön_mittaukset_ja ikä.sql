DROP VIEW "main"."henkilo_mittaus_ika_v2";
CREATE VIEW henkilo_mittaus_ika_v2 AS
SELECT henkilo.henkilo_id, henkilo.sukunimi, henkilo.etunimi, henkilo.sukupuoli, mittaus.mittaus_id, mittaus.pituus, mittaus.paino, (julianday('now') - julianday(henkilo.spaiva))/365 AS ika
FROM henkilo INNER JOIN mittaus ON henkilo.henkilo_id = mittaus.henkilo_id