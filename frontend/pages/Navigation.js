import Link from 'next/link';
import Image from 'next/image';

import styles from '../styles/NavBar.module.css';

function NavBar () {
  return (
    <header className={styles.header}>
      <ul className={styles['nav-site-name']}>
        <li className={styles['sotm-logo']}>State of the Market</li>
      </ul>
      <ul className={styles['nav-page-options']}>
        <Link href="/indicators">Indicators</Link>
        <Link href="/reports">Reports</Link>
      </ul>
      <ul className={styles['nav-options']}>
        <Link href="/login">Login</Link>
        <Link href="/signup">Sign Up</Link>
      </ul>
    </header>
  )
}

export default NavBar;
