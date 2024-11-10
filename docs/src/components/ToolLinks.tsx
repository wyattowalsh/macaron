import { AnimatePresence, motion } from "framer-motion";
import { ChevronDown, ChevronUp } from "lucide-react";
import React, { useState } from "react";
import { FaLink } from "react-icons/fa";
import { linkData } from "../constants/linkData";
import { Button } from "./ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";

interface ToolLink {
	label: string;
	href: string;
	icon?: string;
}

interface ToolLinksProps {
	links: ToolLink[];
}

const ToolLinks: React.FC<ToolLinksProps> = ({ links }) => {
	const [isExpanded, setIsExpanded] = useState(false);

	const toggleExpand = () => setIsExpanded((prev) => !prev);

	return (
		<Card className="rounded-lg shadow-lg border border-primary mb-4">
			<CardHeader className="flex flex-row justify-between items-start p-6">
				<div className="flex items-center gap-2">
					<FaLink aria-hidden="true" className="text-2xl text-primary" />
					<CardTitle className="font-bold text-primary scroll-m-20 text-2xl tracking-tight">
						<h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
							Links
						</h3>
					</CardTitle>
				</div>
				<Button
					variant="ghost"
					onClick={toggleExpand}
					className="p-2 rounded-full hover:bg-muted"
					aria-label={isExpanded ? "Collapse links" : "Expand links"}
				>
					{isExpanded ? <ChevronUp /> : <ChevronDown />}
				</Button>
			</CardHeader>
			<AnimatePresence initial={false}>
				{isExpanded && (
					<motion.div
						initial={{ height: 0, opacity: 0 }}
						animate={{ height: "auto", opacity: 1 }}
						exit={{ height: 0, opacity: 0 }}
						transition={{ duration: 0.3, ease: "easeOut" }}
						className="overflow-hidden"
					>
						<CardContent className="p-6">
							<div className="space-y-4">
								{links.map((link) => {
									const data = linkData[link.label.toLowerCase()] || {};
									const icon =
										link.icon || data.icon || "/img/icons/website.svg";
									return (
										<motion.a
											key={link.href}
											href={link.href}
											target="_blank"
											rel="noopener noreferrer"
											whileHover={{ scale: 1.02 }}
											whileTap={{ scale: 0.98 }}
											className="flex items-center p-4 rounded-md shadow transition-transform transform hover:scale-105 bg-white hover:bg-gray-100"
											style={{
												borderLeft: `4px solid ${data.themeColor || "#845ef7"}`,
											}}
										>
											<img
												src={icon}
												alt={`${link.label} icon`}
												className="w-8 h-8 mr-4"
											/>
											<div>
												<h3 className="text-lg font-medium text-gray-900">
													{link.label}
												</h3>
												<p className="text-sm text-gray-500">
													{new URL(link.href).hostname}
												</p>
											</div>
										</motion.a>
									);
								})}
							</div>
						</CardContent>
					</motion.div>
				)}
			</AnimatePresence>
		</Card>
	);
};

export default ToolLinks;
