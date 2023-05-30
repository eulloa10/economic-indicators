import Link from 'next/link';
import Image from 'next/image';

import styles from '../styles/NavBar.module.css';
import userIcon from '../public/user-icon.png';

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
      {/* <ul className={styles['nav-options']}>
        <Link href="/login">Login</Link>
        <Link href="/signup">Sign Up</Link>
      </ul> */}
      <div className={styles['nav-options']}>
        <button className={styles['user-btn']}>
          <div>
            <Image className={styles['user-icon']} src={userIcon} alt="user"/>
          </div>
          <div className={styles['sign-in-text']}>
            Sign In
          </div>
        </button>
      </div>
    </header>
  )
}

export default NavBar;
