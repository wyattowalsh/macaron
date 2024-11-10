import { Button } from "@site/src/components/ui/button"; // ShadCN Button
import { Card } from "@site/src/components/ui/card"; // ShadCN Card
import { AnimatePresence, motion } from "framer-motion";
import { ChevronDown, ChevronUp } from "lucide-react"; // For toggle icons
import React, { useState } from "react";
import { FaLink } from "react-icons/fa";

interface Link {
	label: string;
	icon: string;
	href: string;
	themeColor?: string; // New field for theme color
}

interface ToolLinksProps {
	links: Link[];
}

const ToolLinks: React.FC<ToolLinksProps> = ({ links }) => {
	const [isExpanded, setIsExpanded] = useState(false);

	const toggleExpand = () => {
		setIsExpanded(!isExpanded);
	};

	return (
		<Card className="p-6 bg-background dark:bg-card rounded-lg shadow-lg border border-primary">
			{/* Title with toggle button */}
			<div className="flex justify-between items-center mb-3">
				<div className="flex items-center gap-2">
					<FaLink className="text-2xl text-primary" />
					<h2 className="text-xl font-semibold text-primary">Links</h2>
				</div>
				<Button
					variant="ghost"
					onClick={toggleExpand}
					className="p-2 rounded-full hover:bg-muted"
				>
					{isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
				</Button>
			</div>

			{/* Collapsible section */}
			<AnimatePresence initial={false}>
				{isExpanded && (
					<motion.div
						initial={{ height: 0, opacity: 0 }}
						animate={{ height: "auto", opacity: 1 }}
						exit={{ height: 0, opacity: 0 }}
						transition={{ duration: 0.4, ease: "easeInOut" }}
						className="overflow-hidden"
					>
						<div className="mt-4 space-y-4">
							{links.map((link, index) => (
								<motion.div
									key={index}
									whileHover={{ scale: 1.02 }}
									whileTap={{ scale: 0.98 }}
									className="flex justify-between items-center p-3 rounded-md shadow-md hover:shadow-lg transition-all"
									style={{
										borderLeft: `4px solid ${link.themeColor || "#845ef7"}`, // Applying theme color
										backgroundColor: `${
											link.themeColor
												? `${link.themeColor}1A`
												: "rgba(132, 94, 247, 0.1)"
										}`, // Subtle background color using alpha
									}}
								>
									<div className="flex items-center gap-3">
										<img src={link.icon} alt={link.label} className="w-6 h-6" />
										<span className="text-sm font-medium text-foreground dark:text-muted-foreground">
											{link.label}
										</span>
									</div>
									{/* Link name flush right */}
									<span className="text-xs text-muted dark:text-muted-foreground">
										{new URL(link.href).hostname}
									</span>
								</motion.div>
							))}
						</div>
					</motion.div>
				)}
			</AnimatePresence>
		</Card>
	);
};

export default ToolLinks;
