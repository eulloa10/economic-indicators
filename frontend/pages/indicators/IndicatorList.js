import styles from '../../styles/IndicatorList/IndicatorList.module.css';

let indicators = [1, 2, 3, 4, 5]

function IndicatorList() {
  return (
    <ul>
      {
        indicators.map(indicator => (
          <li className={styles.indicator} key={indicator}>
            {indicator}
          </li>
        ))
      }
    </ul>
  )
}

export default IndicatorList;
