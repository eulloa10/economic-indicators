import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';

import SignInModal from './SignInModal';
import styles from '../styles/NavBar.module.css';
import userIcon from '../public/user-icon.png';


function NavBar () {
  const [showSignIn, setShowSignIn] = useState(false);

  return (
    <>
      <header className={styles.header}>
        <ul className={styles['nav-site-name']}>
          <li className={styles['sotm-logo']}>State of the Market</li>
        </ul>
        <ul className={styles['nav-page-options']}>
          <Link className={styles['nav-links']} href="/indicators">Indicators</Link>
          <Link className={styles['nav-links']} href="/dashboard">Dashboard</Link>
          <Link className={styles['nav-links']} href="/reports">Reports</Link>
        </ul>
        <div className={styles['nav-options']}>
          <button onClick={() => setShowSignIn(true)} className={styles['user-btn']}>
            <div>
              <Image className={styles['user-icon']} src={userIcon} alt="user"/>
            </div>
            <div className={styles['sign-in-text']}>
              Sign In
            </div>
          </button>
        </div>
      </header>
      {showSignIn && <SignInModal setShowSignIn={setShowSignIn} />}
    </>
  )
}

export default NavBar;
