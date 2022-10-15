import { useState, useEffect } from 'react'

import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Router from "next/router";
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown'
import Button from 'react-bootstrap/Button';

export default function EmissionsCalc() {



    return (
        <>
    
          <Head>
            <title>Emissions Calculator</title>
            <meta name="description" content="Emissions Calc" />
            <link rel="icon" href="/favicon.svg" />
          </Head>
    
          <Container>
            Emissions Calculator
          </Container>
          </>
    )
}