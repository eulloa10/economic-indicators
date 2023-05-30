import Link from 'next/link';
import Image from 'next/image';

import styles from '../styles/NavBar.module.css';

function NavBar () {
  return (
    <header className={styles.header}>
      <ul>
        <li>State of the Market</li>
        <li>
          <Image src="" alt="" />
        </li>
      </ul>
      <ul>
        <Link href="/login">Login</Link>
        <Link href="/signup">Sign Up</Link>
        <Link href="guest">Guest</Link>
      </ul>
    </header>
  )
}

export default NavBar;
