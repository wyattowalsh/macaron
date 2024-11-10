import clsx from "clsx";
import { motion } from "framer-motion";
import styles from "./index.module.scss";

type FeatureItem = {
	img: string;
};

const FeatureList: FeatureItem[] = [
	{
		img: "img/macaron-1.webp",
	},
	{
		img: "img/macaron-2.webp",
	},
	{
		img: "img/macaron-3.webp",
	},
];

function Feature({ img }: FeatureItem) {
	return (
		<div className={styles.feature}>
			<div className="text--center">
				<motion.img
					src={img}
					className={styles.featureImage}
					alt="Feature"
					whileHover={{ scale: 1.02 }}
					transition={{ duration: 0.3 }}
				/>
			</div>
		</div>
	);
}

export default function HomepageFeatures(): JSX.Element {
	return (
		<section className={styles.featuresSection}>
			<div className={clsx(styles.featuresContainer, styles.features)}>
				<div className={clsx("row", styles.featuresRow)}>
					{FeatureList.map((props, idx) => (
						<Feature key={idx} {...props} />
					))}
				</div>
			</div>
		</section>
	);
}
