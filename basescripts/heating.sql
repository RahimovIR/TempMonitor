--
-- PostgreSQL database dump
--

-- Started on 2011-02-03 22:05:30 YEKT

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- TOC entry 1777 (class 1262 OID 16384)
-- Name: heating; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE ROLE tempuser LOGIN
  PASSWORD 'password'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE;

CREATE DATABASE heating WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'ru_RU.utf8' LC_CTYPE = 'ru_RU.utf8';


ALTER DATABASE heating OWNER TO postgres;

\connect heating

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- TOC entry 1491 (class 1259 OID 16464)
-- Dependencies: 3
-- Name: temperature_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE temperature_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.temperature_seq OWNER TO postgres;

--
-- TOC entry 1780 (class 0 OID 0)
-- Dependencies: 1491
-- Name: temperature_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('temperature_seq', 1, false);


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 1492 (class 1259 OID 16466)
-- Dependencies: 1770 1771 3
-- Name: temperature; Type: TABLE; Schema: public; Owner: tempuser; Tablespace: 
--

CREATE TABLE temperature (
    id integer DEFAULT nextval('temperature_seq'::regclass) NOT NULL,
    datetime timestamp with time zone,
    temp real DEFAULT (-200)
);


ALTER TABLE public.temperature OWNER TO tempuser;

--
-- TOC entry 1774 (class 0 OID 16466)
-- Dependencies: 1492
-- Data for Name: temperature; Type: TABLE DATA; Schema: public; Owner: tempuser
--

COPY temperature (id, datetime, temp) FROM stdin;
\.


--
-- TOC entry 1773 (class 2606 OID 16472)
-- Dependencies: 1492 1492
-- Name: temperature_pkey; Type: CONSTRAINT; Schema: public; Owner: tempuser; Tablespace: 
--

ALTER TABLE ONLY temperature
    ADD CONSTRAINT temperature_pkey PRIMARY KEY (id);


--
-- TOC entry 1779 (class 0 OID 0)
-- Dependencies: 3
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2011-02-03 22:05:30 YEKT

--
-- PostgreSQL database dump complete
--

GRANT UPDATE ON TABLE temperature_seq TO tempuser;
