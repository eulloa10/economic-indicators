import Head from 'next/head'
import styles from '@/styles/Home.module.css'

import Navigation from './Navigation';
import Footer from './Footer';
import Landing from './Landing';

export default function Home() {
  return (
    <>
      <Navigation />
      <Landing />
      <Footer />
    </>
  )
}
