import Head from 'next/head'
import styles from '@/styles/Home.module.css'

import Navigation from './Navigation';
import Footer from './Footer';

export default function Home() {
  return (
    <>
      <Navigation />
      <h1>
        Home Page
      </h1>
      <Footer />
    </>
  )
}
