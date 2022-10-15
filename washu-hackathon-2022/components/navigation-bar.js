import React, { useState, useEffect } from "react";
import { useRouter } from 'next/router';

import Router from "next/router";
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown'
import Button from 'react-bootstrap/Button';

import Link from 'next/link'


export default function NavigationBar() {

  const router = useRouter();

  return (
    <Navbar bg="dark" variant="dark">
    <Container>
      <Navbar.Brand href="#home">
        <img
          alt=""
          src="/hackwashulogo.png"
          width="30"
          height="30"
          className="d-inline-block align-top"
        />{' '}
        HACK WASHU 2022
      </Navbar.Brand>
    </Container>
  </Navbar>
  );
}