import Head from 'next/head'

import IndicatorList from './IndicatorList';
import NavBar from '../Navigation';
import Footer from '../Footer';

export default function Indicators() {
  return (
    <>
      <NavBar />
      <IndicatorList />
      <Footer />
    </>
  )
}
