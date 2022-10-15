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
import Form from 'react-bootstrap/Form';


export default function EmissionsCalc() {

    const [gallonsOfGas, setGallonsOfGas] = useState(0.0);

    const [poundsOfCO2, setPoundsOfCO2] = useState(0.0);

    // 19.6 lbs CO2 per gallon
    function calculateEmissions() {
        setPoundsOfCO2(gallonsOfGas * 19.6);
    }

    return (
        <>
    
          <Head>
            <title>Emissions Calculator</title>
            <meta name="description" content="Emissions Calc" />
            <link rel="icon" href="/favicon.svg" />
          </Head>
    
          <Container>
            Emissions Calculator

            <Form.Control 
            type="number" 
            className="mt-3" 
            placeholder="Number of gallons" 
            value={gallonsOfGas}
            onChange={(event) => {
                setGallonsOfGas(event.target.value);
              }}
            
            />
            <Button 
            variant="primary" 
            className="mt-3"
            onClick={calculateEmissions}
            >
                Calculate CO2
            </Button>

              <p>Lbs of CO2 emitted: <b>{poundsOfCO2}</b></p>
          </Container>
          </>
    )
}