import Link from 'next/link';
import Image from 'next/image';

import styles from '../styles/Footer.module.css';
import githubLogo from '../public/github.png';

function Footer () {
  return (
    <footer className={styles.footer}>
      <ul className={styles.footerList}>
        <li>2023</li>
        <li className={styles.link}>
          <a href="https://github.com/eulloa10" target="_blank">
            <Image className={styles.githubLogo} src={githubLogo} alt="github" />
          </a>
        </li>
      </ul>
    </footer>
  )
}

export default Footer;
