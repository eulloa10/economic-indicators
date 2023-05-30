import '@/styles/globals.css'
import { Roboto_Mono } from '@next/font/google';

const roboto_mono = Roboto_Mono({ subsets: ['latin'] });

export default function App({ Component, pageProps }) {

  return (
    <main className={roboto_mono.className}>
      <Component {...pageProps} />
    </main>
    )
}
